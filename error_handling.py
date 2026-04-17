"""Error handling utilities."""

def safe_webhook_process(handler, payload):
    """Wrap webhook handler with error handling."""
    try:
        return handler(payload)
    except ValueError as e:
        return {"status": "error", "reason": str(e)}
    except Exception as e:
        return {"status": "error", "reason": "unexpected: " + str(e)}
