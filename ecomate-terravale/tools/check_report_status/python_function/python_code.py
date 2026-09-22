def check_report_status(reference_number: str) -> dict:
    """Looks up the current status of a filed Terravale report by its reference number.

    Args:
        reference_number: The report reference, e.g. 'ECO-2274' or 'ACC-3106'.

    Returns:
        dict: The reference, a status, and a plain-language note. If the reference
        is not a valid ECO- or ACC- reference, returns an error status.
    """
    ref = reference_number.strip().upper()
    if not (ref.startswith("ECO-") or ref.startswith("ACC-")) or len(ref) != 8:
        return {"reference_number": ref, "status": "invalid",
                "note": "That does not look like a valid ECO or ACC reference."}
    # Mock lifecycle: derive a repeatable status from the reference digits so tests are stable
    digit_sum = sum(int(c) for c in ref if c.isdigit())
    states = ["Received", "In review", "Actioned"]
    status = states[digit_sum % 3]
    team = "facilities team" if ref.startswith("ECO-") else "accessibility team"
    return {"reference_number": ref, "status": status,
            "note": f"Your report is currently '{status}' with the {team}."}