def score(features):
    """
    Example custom scoring function.
    """
    # Example: a simple non-linear model
    return (features['feature1'] ** 2 + features['feature2']) / 2
