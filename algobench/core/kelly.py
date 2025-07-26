def kelly_fraction(p: float, b: float) -> float:
    """
    Calculates the optimal fraction of capital to allocate using the Kelly Criterion.
    """
    if b <= 0:
        return 0
    return max((b * p - (1 - p)) / b, 0)
