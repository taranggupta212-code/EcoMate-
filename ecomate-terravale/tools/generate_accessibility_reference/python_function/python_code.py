import random

def generate_accessibility_reference() -> dict:
    """Generates a unique accessibility report reference number in the format ACC-XXXX.

    Returns:
        dict: A dictionary with a single key 'reference_number' whose value is a
        string like 'ACC-3106' (ACC- followed by four random digits).
    """
    number = random.randint(1000, 9999)
    return {"reference_number": f"ACC-{number}"}