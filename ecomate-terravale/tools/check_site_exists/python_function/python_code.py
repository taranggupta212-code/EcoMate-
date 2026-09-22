def check_site_exists(site_name: str) -> dict:
    """Checks whether a reported location matches a known Terravale Facilities Group site.

    Args:
        site_name: The site or location the staff member named.

    Returns:
        dict: valid True with the matched site name if it is a known Terravale site,
        or valid False with the list of known sites if it is not recognised.
    """
    known_sites = ["Sunshine", "Altona", "Laverton", "Sunshine West", "Truganina", "Derrimut"]
    text = site_name.strip().lower()
    for site in known_sites:
        if site.lower() in text:
            return {"valid": True, "matched_site": site,
                    "note": f"Matched Terravale site: {site}."}
    return {"valid": False, "matched_site": None,
            "known_sites": known_sites,
            "note": "That location is not a recognised Terravale site."}