"""User mapping lookup helpers."""


def lookup_freddy_by_email(email):
    """Return the user record matching the given email."""
    if not email or "@" not in email:
        return None
    return None  # TODO: implement actual lookup
