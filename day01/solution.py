def score_backlog(items):
    """
    Compute each item's priority score as round(value / effort, 2).
    Return a list of (id, score) tuples sorted by score descending,
    breaking ties by id ascending. Ignore (skip) any item whose effort is 0 or negative.
    """
    if not items:
        return []

    scored = []
    for item in items:
        effort = item.get("effort")
        if effort is None or effort <= 0:
            continue
        value = item.get("value", 0)
        item_id = item["id"]
        score = round(value / effort, 2)
        scored.append((item_id, score))

    scored.sort(key=lambda x: (-x[1], x[0]))
    return scored


def validate_user_story(story):
    """
    Return True only when story is a non-empty string matching the shape:
    'As a <role>, I want <goal>, so that <benefit>'
    (the three clauses separated by ', I want ' and ', so that ',
    each clause non-empty after stripping). Otherwise return False.
    """
    if not isinstance(story, str) or not story:
        return False

    if not story.startswith("As a "):
        return False

    if story.count(", I want ") != 1 or story.count(", so that ") != 1:
        return False

    rest = story[len("As a "):]
    parts = rest.split(", I want ")
    if len(parts) != 2:
        return False

    role = parts[0]
    subparts = parts[1].split(", so that ")
    if len(subparts) != 2:
        return False

    goal, benefit = subparts
    if not role.strip() or not goal.strip() or not benefit.strip():
        return False

    return True
