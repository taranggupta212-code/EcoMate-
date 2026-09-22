import random

def generate_reference_number() -> dict:
    """Generates a unique incident reference number in the format ECO-XXXX and stores it for later recall.

    Returns:
        dict: A dictionary containing the reference number under both the
        reference_number key and the last_reference_number key.
    """
    number = random.randint(1000, 9999)
    ref = f"ECO-{number}"
    return {"reference_number": ref, "last_reference_number": ref}