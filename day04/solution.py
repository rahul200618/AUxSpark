import re


def parse_requirement(line):
    """
    Strip the line. Return None for a blank line or a comment (starts with #).
    Otherwise return a tuple (name, operator, version) where operator is one of
    ==, >=, <=. If the line has a name but no recognised operator, return (name, '', '').
    """
    if not isinstance(line, str):
        return None

    line = line.strip()
    if not line or line.startswith("#"):
        return None

    for op in ("==", ">=", "<="):
        if op in line:
            name, version = line.split(op, 1)
            return (name.strip(), op, version.strip())

    match = re.match(r"^([^<>=~! ]+)", line)
    name = match.group(1).strip() if match else line
    return (name, "", "")


def find_unpinned(lines):
    """
    Return a sorted list of package names that are not pinned with ==
    (including bare names with no operator). Blanks and comments are ignored.
    """
    if not lines:
        return []

    unpinned = []
    for line in lines:
        parsed = parse_requirement(line)
        if parsed is not None and parsed[1] != "==":
            unpinned.append(parsed[0])

    return sorted(unpinned)


def resolve_versions(lines):
    """
    Return a sorted list of (name, version) tuples for every ==-pinned package.
    """
    if not lines:
        return []

    resolved = []
    for line in lines:
        parsed = parse_requirement(line)
        if parsed is not None and parsed[1] == "==":
            resolved.append((parsed[0], parsed[2]))

    return sorted(resolved)
