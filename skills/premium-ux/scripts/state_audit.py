#!/usr/bin/env python3
"""
state_audit.py - find UI code that fetches data but may not handle its states.

Part of the premium-ux skill. Scans a codebase for data-fetching sites and reports
which files appear to lack loading, error, or empty handling. Also flags generic
error copy, swallowed exceptions, and log-only error handling.

This is a heuristic grep, not a type checker. It produces CANDIDATES to read, not
findings to report. A flagged file may legitimately delegate state to a parent; an
unflagged file may handle states badly. Use it to decide where to look.

Zero dependencies. Python 3.8+.

Usage:
    python3 state_audit.py --path /path/to/repo
    python3 state_audit.py --path . --format json --out findings.json
    python3 state_audit.py --path . --ext .tsx,.ts --min-severity high
"""

import argparse
import json
import os
import re
import sys
from collections import OrderedDict

IGNORE_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "bower_components", "vendor",
    "build", "dist", "out", "target", ".next", ".nuxt", ".svelte-kit",
    ".output", "coverage", "__pycache__", ".venv", "venv", "env",
    "Pods", "Carthage", ".gradle", ".idea", ".vscode", ".dart_tool",
    "DerivedData", ".expo", ".turbo", ".parcel-cache", "storybook-static",
    "android/app/build", "ios/build", "generated", "__generated__",
}

IGNORE_FILE_RE = re.compile(
    r"(\.min\.|\.bundle\.|\.lock$|\.map$|\.d\.ts$|"
    r"\.(test|spec|stories|e2e|mock|mocks|fixture|fixtures)\.|"
    r"(^|/)(jest|vitest|webpack|rollup|vite|babel|metro|tailwind|eslint)\.config\.)",
    re.IGNORECASE,
)

# ---------------------------------------------------------------- stack rules

WEB = {
    "exts": {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte", ".astro"},
    "fetch": [
        r"\buse(?:Suspense)?Query\s*[(<]", r"\buseInfiniteQuery\s*[(<]",
        r"\buseMutation\s*[(<]", r"\buseSWR(?:Infinite|Mutation)?\s*\(",
        r"\buseFetch\s*\(", r"\buseAsyncData\s*\(", r"\buseLazyQuery\s*\(",
        r"(?<!\.)\bfetch\s*\(", r"\baxios\s*(?:\.\s*\w+)?\s*\(",
        r"\bsupabase\s*\.\s*(?:from|rpc|storage|functions)\s*\(",
        r"\bcreateAsyncThunk\s*\(", r"\bgetDocs?\s*\(", r"\bonSnapshot\s*\(",
        r"\bprisma\s*\.\s*\w+\s*\.\s*(?:find|create|update|delete)",
        r"\btrpc\s*\.", r"\bapi\s*\.\s*(?:get|post|put|patch|delete)\s*\(",
    ],
    "loading": [
        r"\bis(?:Loading|Pending|Fetching|Validating|Submitting|Refetching)\b",
        r"\bloading\b", r"\bpending\b", r"\bSkeleton\b", r"\bSpinner\b",
        r"\bActivityIndicator\b", r"\bCircularProgress\b", r"\bShimmer\b",
        r"\bProgressBar\b", r"<Suspense", r"\bfallback\s*[=:]", r"\bstatus\s*===?\s*[\"']loading",
    ],
    "error": [
        r"\bis(?:Error|Rejected)\b", r"\bhasError\b", r"\bonError\b",
        r"\berrorMessage\b", r"\bErrorBoundary\b", r"\bErrorState\b",
        r"\.catch\s*\(", r"\bcatch\s*\(", r"\bcatch\s*\{",
        r"\berror\s*[&?:)\].,}]", r"\berror\s*===?", r"\bstatus\s*===?\s*[\"']error",
    ],
    "empty": [
        r"\.length\s*===?\s*0", r"\.length\s*<\s*1", r"\.length\s*\?",
        r"!\s*\w+(?:\?)?\.length", r"\bisEmpty\b", r"\bEmptyState\b",
        r"\bListEmptyComponent\b", r"\bNoResults?\b", r"\bEmptyPlaceholder\b",
        r"\.count\s*===?\s*0", r"\.size\s*===?\s*0", r"length\s*>\s*0\s*\?",
    ],
}

SWIFT = {
    "exts": {".swift"},
    "fetch": [
        r"\bURLSession\b", r"\.task\s*\{", r"\bTask\s*\{", r"\btry\s+await\b",
        r"\basync\s+func\b", r"\bAsyncStream\b", r"\bdataTask\b",
    ],
    "loading": [r"\bisLoading\b", r"\bProgressView\b", r"\.redacted\b", r"\bisFetching\b", r"\bcase\s+loading\b"],
    "error": [r"\bcatch\b", r"\bResult<", r"\.failure\b", r"\.alert\b", r"\bError\b"],
    "empty": [r"\.isEmpty\b", r"\.count\s*==\s*0", r"\bContentUnavailableView\b", r"\bEmptyState\b"],
}

KOTLIN = {
    "exts": {".kt", ".kts", ".java"},
    "fetch": [
        r"\bviewModelScope\s*\.\s*launch", r"\bsuspend\s+fun\b", r"\bRetrofit\b",
        r"\bResponse<", r"\bflow\s*\{", r"\.collectAsState", r"\bHttpClient\b",
        r"\blifecycleScope\s*\.\s*launch",
    ],
    "loading": [r"\bisLoading\b", r"\bLoading\b", r"\bCircularProgressIndicator\b", r"\bShimmer\b", r"\bprogress\b"],
    "error": [r"\bcatch\s*\(", r"\bResult\s*\.\s*failure", r"\bonFailure\b", r"\bError\b", r"\brunCatching\b"],
    "empty": [r"\.isEmpty\(\)", r"\bisEmpty\b", r"\.size\s*==\s*0", r"\bEmptyState\b", r"\.none\b"],
}

DART = {
    "exts": {".dart"},
    "fetch": [
        r"\bFutureBuilder\b", r"\bStreamBuilder\b", r"\bhttp\s*\.\s*\w+\s*\(",
        r"\bawait\b", r"\bFuture<", r"\bdio\s*\.", r"\.watch\s*\(", r"\bref\.watch\b",
    ],
    "loading": [
        r"ConnectionState\s*\.\s*waiting", r"\bCircularProgressIndicator\b",
        r"\bisLoading\b", r"\bShimmer\b", r"\bAsyncLoading\b", r"\bLinearProgressIndicator\b",
    ],
    "error": [r"\bhasError\b", r"\bcatch\b", r"\}\s*on\s+\w+", r"\bonError\b", r"\bAsyncError\b", r"\bErrorWidget\b"],
    "empty": [r"\.isEmpty\b", r"\.length\s*==\s*0", r"\bEmptyState\b"],
}

STACKS = [("web", WEB), ("swift", SWIFT), ("kotlin", KOTLIN), ("dart", DART)]

# ------------------------------------------------------------ copy/code smells

GENERIC_ERROR_COPY = re.compile(
    r"[\"'`]([^\"'`\n]{0,40}?"
    r"(?:something went wrong|an error (?:has )?occurred|an error occured|unknown error|"
    r"oops[!., ]|unexpected error|failed to load|something broke|try again later|"
    r"error occurred|please try again|generic error)"
    r"[^\"'`\n]{0,40})[\"'`]",
    re.IGNORECASE,
)

PLACEHOLDER_COPY = re.compile(
    r"[\"'`]([^\"'`\n]{0,60}?(?:lorem ipsum|coming soon|placeholder text|"
    r"your text here|insert .{0,20} here|\btbd\b)[^\"'`\n]{0,40})[\"'`]",
    re.IGNORECASE,
)

# Code markers are matched case-sensitively and word-bounded, so identifiers like
# "toDone" or "fixmeasure" don't register as placeholder copy.
PLACEHOLDER_MARKER = re.compile(
    r"[\"'`]([^\"'`\n]{0,60}?\b(?:TODO|FIXME|XXX|HACK)\b[^\"'`\n]{0,40})[\"'`]"
)

SWALLOWED = re.compile(
    r"(?:catch\s*(?:\([^)]*\))?\s*\{\s*\}"
    r"|\.catch\s*\(\s*(?:\([^)]*\)|\w+)?\s*=>\s*\{\s*\}\s*\)"
    r"|catch\s*\([^)]*\)\s*\{\s*(?://[^\n]*\s*)?\}"
    r"|except\s*:\s*pass)"
)

CATCH_START = re.compile(r"\bcatch\b\s*(?:\([^)]*\))?\s*\{")
# things that count as "actually handled"
HANDLED_HINTS = re.compile(
    r"\b(?:set\w*(?:Error|State|Status|Message)|throw|rethrow|toast|notify|Alert|alert|"
    r"dispatch|showError|captureException|Sentry|reportError|onError|reject|return\s+\w)",
    re.IGNORECASE,
)
LOG_ONLY = re.compile(r"console\s*\.\s*(?:error|log|warn)|print\s*\(|debugPrint\s*\(|NSLog|Log\s*\.\s*[dewi]\s*\(")


def pick_stack(ext):
    for name, rules in STACKS:
        if ext in rules["exts"]:
            return name, rules
    return None, None


def compile_rules():
    for _, rules in STACKS:
        for key in ("fetch", "loading", "error", "empty"):
            rules[key + "_re"] = [re.compile(p) for p in rules[key]]


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def should_skip_dir(dirpath, root):
    rel = os.path.relpath(dirpath, root)
    parts = set(rel.split(os.sep))
    return bool(parts & IGNORE_DIRS)


def scan_file(path, rel, rules, stack):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except (OSError, IOError):
        return None
    if len(text) > 800_000:
        return None

    fetch_hits = []
    for rx in rules["fetch_re"]:
        m = rx.search(text)
        if m:
            fetch_hits.append((rx.pattern, line_of(text, m.start())))

    result = {
        "file": rel,
        "stack": stack,
        "fetches": len(fetch_hits),
        "fetch_line": fetch_hits[0][1] if fetch_hits else None,
        "missing": [],
        "generic_copy": [],
        "placeholder_copy": [],
        "swallowed": [],
        "log_only": [],
    }

    if fetch_hits:
        # an empty catch is not error handling, so it can't count as one
        state_text = SWALLOWED.sub(" ", text)
        for key in ("loading", "error", "empty"):
            if not any(rx.search(state_text) for rx in rules[key + "_re"]):
                result["missing"].append(key)

    for m in GENERIC_ERROR_COPY.finditer(text):
        result["generic_copy"].append({"line": line_of(text, m.start()), "text": m.group(1).strip()})
    for rx in (PLACEHOLDER_COPY, PLACEHOLDER_MARKER):
        for m in rx.finditer(text):
            result["placeholder_copy"].append(
                {"line": line_of(text, m.start()), "text": m.group(1).strip()}
            )
    for m in SWALLOWED.finditer(text):
        result["swallowed"].append({"line": line_of(text, m.start())})

    for m in CATCH_START.finditer(text):
        body = text[m.end():m.end() + 260]
        brace = body.find("}")
        if brace != -1:
            body = body[:brace]
        if LOG_ONLY.search(body) and not HANDLED_HINTS.search(body):
            result["log_only"].append({"line": line_of(text, m.start())})

    interesting = (
        result["missing"] or result["generic_copy"] or result["placeholder_copy"]
        or result["swallowed"] or result["log_only"]
    )
    return result if interesting or fetch_hits else None


def walk(root, exts):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]
        if should_skip_dir(dirpath, root):
            continue
        for fn in filenames:
            ext = os.path.splitext(fn)[1]
            if exts and ext not in exts:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            if IGNORE_FILE_RE.search(rel.replace(os.sep, "/")):
                continue
            stack, rules = pick_stack(ext)
            if not rules:
                continue
            yield full, rel, rules, stack


def severity(entry):
    miss = set(entry["missing"])
    if {"loading", "error"} <= miss or entry["swallowed"]:
        return "high"
    if miss or entry["log_only"] or entry["generic_copy"] or entry["placeholder_copy"]:
        return "medium"
    return "low"


def render_markdown(results, stats, root):
    L = []
    a = L.append
    a("# State coverage scan")
    a("")
    a("Heuristic scan for data-fetching code that may not handle its states.")
    a("**Every row is a candidate to read, not a confirmed finding.** A file may legitimately")
    a("delegate state to a parent component.")
    a("")
    a(f"**Root:** `{root}`")
    a("")
    a("## Summary")
    a("")
    a(f"- Files scanned: **{stats['scanned']}**")
    a(f"- Files with data fetching: **{stats['with_fetch']}**")
    a(f"- …missing a loading state: **{stats['miss_loading']}**")
    a(f"- …missing an error state: **{stats['miss_error']}**")
    a(f"- …missing an empty state: **{stats['miss_empty']}**")
    if stats["with_fetch"]:
        a(f"- Apparent state coverage: **{stats['coverage']}%** "
          f"(fetching files with all three signals present)")
    a(f"- Generic error strings: **{stats['generic']}**")
    a(f"- Swallowed exceptions: **{stats['swallowed']}**")
    a(f"- Log-only error handling: **{stats['log_only']}**")
    a(f"- Placeholder copy: **{stats['placeholder']}**")
    a("")

    buckets = OrderedDict([("high", []), ("medium", [])])
    for r in results:
        sev = severity(r)
        if sev in buckets:
            buckets[sev].append(r)

    for sev, rows in buckets.items():
        if not rows:
            continue
        a(f"## {sev.title()} priority ({len(rows)})")
        a("")
        a("| File | Missing | Other signals |")
        a("|---|---|---|")
        for r in sorted(rows, key=lambda x: (-len(x["missing"]), x["file"]))[:200]:
            missing = ", ".join(r["missing"]) or "—"
            extra = []
            if r["swallowed"]:
                extra.append(f"{len(r['swallowed'])} swallowed")
            if r["log_only"]:
                extra.append(f"{len(r['log_only'])} log-only")
            if r["generic_copy"]:
                extra.append(f"{len(r['generic_copy'])} generic copy")
            if r["placeholder_copy"]:
                extra.append(f"{len(r['placeholder_copy'])} placeholder")
            loc = f"`{r['file']}`"
            if r["fetch_line"]:
                loc += f":{r['fetch_line']}"
            a(f"| {loc} | {missing} | {', '.join(extra) or '—'} |")
        a("")

    def detail_section(title, key, note):
        rows = [(r["file"], h) for r in results for h in r[key]]
        if not rows:
            return
        a(f"## {title} ({len(rows)})")
        a("")
        a(note)
        a("")
        for f, h in rows[:120]:
            txt = h.get("text")
            if txt:
                a(f"- `{f}:{h['line']}` — \"{txt}\"")
            else:
                a(f"- `{f}:{h['line']}`")
        if len(rows) > 120:
            a(f"- …and {len(rows) - 120} more")
        a("")

    detail_section(
        "Generic error copy", "generic_copy",
        "The system usually knows more than this. Replace with what happened, why, and the next "
        "action — see `references/state-coverage.md`.",
    )
    detail_section(
        "Swallowed exceptions", "swallowed",
        "An empty catch means a failure the user is never told about. These are the states that "
        "produce 'nothing happened when I tapped it'.",
    )
    detail_section(
        "Log-only error handling", "log_only",
        "The error reaches the console but apparently never reaches the user or any error state.",
    )
    detail_section(
        "Placeholder copy", "placeholder_copy",
        "Unfinished strings in shipped surfaces are one of the strongest cheap-feeling signals.",
    )

    a("## Caveats")
    a("")
    a("- Detection is file-level and regex-based; a parent may handle what a child omits.")
    a("- Presence of a keyword is not proof the state is handled *well* — a `Spinner` that never")
    a("  resolves still counts as present here.")
    a("- Read every candidate before putting it in a report.")
    a("- The coverage percentage is a conversation starter, not a score to optimize.")
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description="Scan a codebase for missing UI state handling.")
    p.add_argument("--path", default=".", help="root directory to scan (default: .)")
    p.add_argument("--format", choices=["md", "json"], default="md", help="output format")
    p.add_argument("--out", help="write to this file instead of stdout")
    p.add_argument("--ext", help="comma-separated extensions to restrict to, e.g. .tsx,.ts")
    p.add_argument("--min-severity", choices=["high", "medium", "low"], default="medium",
                   help="omit candidates below this severity (default: medium)")
    args = p.parse_args()

    root = os.path.abspath(os.path.expanduser(args.path))
    if not os.path.isdir(root):
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2

    compile_rules()
    exts = set()
    if args.ext:
        exts = {e if e.startswith(".") else "." + e for e in args.ext.split(",") if e.strip()}

    order = {"high": 3, "medium": 2, "low": 1}
    floor = order[args.min_severity]

    all_results, scanned = [], 0
    for full, rel, rules, stack in walk(root, exts):
        scanned += 1
        r = scan_file(full, rel, rules, stack)
        if r:
            all_results.append(r)

    # Stats are computed over every file scanned, before the severity filter, so
    # the coverage figure reflects the codebase rather than the reported subset.
    with_fetch = [r for r in all_results if r["fetches"]]
    results = [r for r in all_results if order[severity(r)] >= floor]
    full_cov = [r for r in with_fetch if not r["missing"]]
    stats = {
        "scanned": scanned,
        "with_fetch": len(with_fetch),
        "miss_loading": sum(1 for r in with_fetch if "loading" in r["missing"]),
        "miss_error": sum(1 for r in with_fetch if "error" in r["missing"]),
        "miss_empty": sum(1 for r in with_fetch if "empty" in r["missing"]),
        "coverage": round(100 * len(full_cov) / len(with_fetch)) if with_fetch else 0,
        "generic": sum(len(r["generic_copy"]) for r in all_results),
        "swallowed": sum(len(r["swallowed"]) for r in all_results),
        "log_only": sum(len(r["log_only"]) for r in all_results),
        "placeholder": sum(len(r["placeholder_copy"]) for r in all_results),
    }

    if args.format == "json":
        payload = {"root": root, "stats": stats,
                   "candidates": [dict(r, severity=severity(r)) for r in results]}
        out = json.dumps(payload, indent=2)
    else:
        out = render_markdown(results, stats, root)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(out + "\n")
        print(f"wrote {args.out} ({stats['with_fetch']} fetching files, "
              f"{stats['coverage']}% apparent coverage)")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
