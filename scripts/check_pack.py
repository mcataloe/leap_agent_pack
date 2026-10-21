#!/usr/bin/env python3
"""Static checks for the LEAP Agent Pack. Standard library only.

Usage:
    python3 scripts/check_pack.py
    python3 scripts/check_pack.py --framework ../leap_framework

Checks:
  - every AGENTS template has well-formed, ordered markers
  - template metadata version and date match manifests/latest.json
  - manifest entries exist, and every template/example file is listed
  - the LEAP Core text is identical in the global and combined templates
    (and matches the framework's docs/leap-core.md with --framework)
  - word budgets: LEAP Core <= 650, project section template <= 800
  - relative Markdown links and same-repo anchors resolve
  - CHANGELOG.md has an entry for the manifest version
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE_MAX_WORDS = 650
PROJECT_MAX_WORDS = 800
MARKERS = {
    "managed": ("<!-- LEAP_MANAGED_SECTION_BEGIN -->", "<!-- LEAP_MANAGED_SECTION_END -->"),
    "project": ("<!-- LEAP_PROJECT_SECTION_BEGIN -->", "<!-- LEAP_PROJECT_SECTION_END -->"),
    "local": ("<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->", "<!-- LEAP_LOCAL_OVERRIDES_END -->"),
}
REQUIRED_SECTIONS = {
    "global": ["managed"],
    "repo": ["managed", "project", "local"],
    "combined": ["managed", "project", "local"],
    "repo-example": ["managed", "project"],
}
RETIRED = ("LEAP_MASTER_GLOBAL_SECTION", "LEAP_MASTER_REPO_SECTION")

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def words(text: str) -> int:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    return len(re.findall(r"[A-Za-z0-9][\w'’.-]*", text))


def section(text: str, name: str) -> str | None:
    begin, end = MARKERS[name]
    if text.count(begin) != 1 or text.count(end) != 1:
        return None
    start, stop = text.index(begin), text.index(end)
    return text[start + len(begin):stop] if start < stop else None


def core_text(managed: str) -> str:
    """LEAP Core body: from the '## Purpose' heading to the end of the section."""
    idx = managed.find("## Purpose")
    return managed[idx:].strip() if idx >= 0 else ""


def metadata(text: str) -> dict[str, str]:
    m = re.search(r"LEAP_AGENT_PACK_TEMPLATE:\n(.*?)END_LEAP_AGENT_PACK_TEMPLATE", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        key, _, value = line.strip().partition(":")
        out[key.strip()] = value.strip().strip('"')
    return out


def slug(heading: str) -> str:
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    found, seen = set(), {}
    in_code = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        m = None if in_code else re.match(r"#{1,6}\s+(.*)", line)
        if m:
            base = slug(m.group(1))
            n = seen.get(base, 0)
            seen[base] = n + 1
            found.add(base if n == 0 else f"{base}-{n}")
    return found


def check_links(root: Path) -> None:
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = re.sub(r"(```|~~~).*?\1", "", md.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"[a-z]+:", target):
                continue
            file_part, _, frag = target.partition("#")
            dest = (md.parent / file_part).resolve() if file_part else md
            rel = md.relative_to(root)
            if not dest.exists():
                fail(f"{rel}: broken link -> {target}")
            elif frag and dest.suffix == ".md" and frag not in anchors(dest):
                fail(f"{rel}: missing anchor -> {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--framework", type=Path, help="path to a leap_framework checkout")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "manifests/latest.json").read_text(encoding="utf-8"))
    version, updated = manifest["version"], manifest["lastUpdated"]

    listed = {entry["path"] for entry in manifest["files"]}
    for entry in manifest["files"]:
        if not (ROOT / entry["path"]).is_file():
            fail(f"manifest lists missing file: {entry['path']}")
    for folder in ("templates", "examples"):
        for f in (ROOT / folder).rglob("*.md"):
            rel = f.relative_to(ROOT).as_posix()
            if rel not in listed:
                fail(f"file not listed in manifest: {rel}")

    cores = {}
    for entry in manifest["files"]:
        kind = entry.get("template")
        path = ROOT / entry["path"]
        if not kind or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        meta = metadata(text)
        if meta.get("template") != kind:
            fail(f"{entry['path']}: metadata template '{meta.get('template')}' != '{kind}'")
        if meta.get("version") != version:
            fail(f"{entry['path']}: metadata version '{meta.get('version')}' != manifest '{version}'")
        if meta.get("last_updated") != updated:
            fail(f"{entry['path']}: metadata last_updated '{meta.get('last_updated')}' != manifest '{updated}'")
        for retired in RETIRED:
            if retired in text:
                fail(f"{entry['path']}: retired marker {retired}")
        positions = []
        for name in REQUIRED_SECTIONS.get(kind, []):
            body = section(text, name)
            if body is None:
                fail(f"{entry['path']}: missing or malformed {name} markers")
                continue
            positions.append(text.index(MARKERS[name][0]))
            if name == "managed" and kind in ("global", "combined"):
                cores[kind] = core_text(body)
            if name == "project" and kind in ("repo", "combined") and words(body) > PROJECT_MAX_WORDS:
                fail(f"{entry['path']}: project section is {words(body)} words (> {PROJECT_MAX_WORDS})")
        if positions != sorted(positions):
            fail(f"{entry['path']}: sections out of order")

    if set(cores) == {"global", "combined"}:
        if cores["global"] != cores["combined"]:
            fail("LEAP Core differs between global and combined templates")
        if words(cores["global"]) > CORE_MAX_WORDS:
            fail(f"LEAP Core is {words(cores['global'])} words (> {CORE_MAX_WORDS})")
        if args.framework:
            doc = (args.framework / "docs/leap-core.md").read_text(encoding="utf-8")
            m = re.search(r"<!-- LEAP_CORE_TEXT_BEGIN -->(.*?)<!-- LEAP_CORE_TEXT_END -->", doc, re.S)
            if not m:
                fail("framework docs/leap-core.md: LEAP_CORE_TEXT markers not found")
            elif m.group(1).strip() != cores["global"]:
                fail("LEAP Core in templates differs from framework docs/leap-core.md")
    else:
        fail("could not extract LEAP Core from global and combined templates")

    if f"## {version}" not in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"):
        fail(f"CHANGELOG.md has no '## {version}' entry")

    check_links(ROOT)

    if errors:
        print("\n".join(f"FAIL {e}" for e in errors))
        print(f"\n{len(errors)} problem(s)")
        return 1
    core_words = words(cores.get("global", ""))
    print(f"Agent Pack {version}: PASS (LEAP Core {core_words} words"
          + (", matches framework" if args.framework else "") + ")")
    return 0


if __name__ == "__main__":
    sys.exit(main())
