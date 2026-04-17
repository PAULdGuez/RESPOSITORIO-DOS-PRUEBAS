"""Webhook validation module."""

def validate_webhook_signature(payload, secret):
    """Validate HMAC signature from webhook payload."""
    import hmac, hashlib
    expected = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return expected
