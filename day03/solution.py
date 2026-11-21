import sqlite3


def category_counts(tickets):
    """
    Given a list of dicts like {"id": str, "category": str},
    create a tickets table in an in-memory SQLite database, insert the rows,
    and run a GROUP BY category query.
    Return a list of (category, count) tuples sorted by count descending,
    ties broken by category ascending.
    """
    if not tickets:
        return []

    conn = sqlite3.connect(":memory:")
    try:
        cur = conn.cursor()
        cur.execute("CREATE TABLE tickets (id TEXT, category TEXT)")
        cur.executemany(
            "INSERT INTO tickets (id, category) VALUES (?, ?)",
            [(t.get("id"), t.get("category")) for t in tickets],
        )
        cur.execute(
            "SELECT category, COUNT(*) FROM tickets GROUP BY category ORDER BY COUNT(*) DESC, category ASC"
        )
        return cur.fetchall()
    finally:
        conn.close()


def top_category(tickets):
    """
    Return the single category string with the most tickets
    (ties broken by category ascending). Return None for an empty list.
    """
    if not tickets:
        return None

    counts = category_counts(tickets)
    return counts[0][0] if counts else None
