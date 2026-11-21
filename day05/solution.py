def is_valid(ticket, contract):
    """
    Return True if ticket satisfies contract:
    - Must carry a non-empty id
    - Every field in required is present and non-empty
    - category is in contract['category'] (if defined)
    - priority is in contract['priority'] (if defined)
    """
    if not isinstance(ticket, dict) or not isinstance(contract, dict):
        return False

    ticket_id = ticket.get("id")
    if ticket_id is None or (isinstance(ticket_id, str) and not ticket_id.strip()) or ticket_id == "":
        return False

    for field in contract.get("required", []):
        if field not in ticket:
            return False
        val = ticket[field]
        if val is None or (isinstance(val, str) and not val.strip()):
            return False

    if "category" in contract:
        if ticket.get("category") not in contract["category"]:
            return False

    if "priority" in contract:
        if ticket.get("priority") not in contract["priority"]:
            return False

    return True


def validate_tickets(tickets, contract):
    """
    Validate a list of ticket dicts against a data contract.
    Return a tuple (valid_ids, quarantined_ids) where each list is sorted.
    A ticket with no id (or an empty one) is quarantined under "<no-id>".
    """
    if not tickets:
        return ([], [])

    valid_ids = []
    quarantined_ids = []

    for ticket in tickets:
        ticket_id = ticket.get("id") if isinstance(ticket, dict) else None
        if ticket_id is None or (isinstance(ticket_id, str) and not ticket_id.strip()) or ticket_id == "":
            raw_id = "<no-id>"
        else:
            raw_id = ticket_id

        if is_valid(ticket, contract):
            valid_ids.append(raw_id)
        else:
            quarantined_ids.append(raw_id)

    return (sorted(valid_ids), sorted(quarantined_ids))
