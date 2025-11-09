def is_numeric(value):
    """
    This function check if a string represents any valid number (integer or float, including negatives).
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
