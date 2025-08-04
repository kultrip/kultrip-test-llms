def validate_user(token):
    """
    Stub for user authentication.
    Replace this with real implementation later.
    """
    # For now, return a dummy user object if token is not empty
    if token:
        return {"id": 1, "name": "testuser"}
    return None