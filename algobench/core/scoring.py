import pandas as pd

def linear_model_score(features: pd.Series, weights: dict) -> float:
    """
    Calculates a score based on a linear combination of features and weights.
    Assumes features not in weights have a weight of 0.
    """
    score = 0.0
    for feature, value in features.items():
        score += weights.get(feature, 0) * value
    
    # Normalize to a probability (0-1) using a sigmoid-like function for simplicity
    # A proper implementation might use a more robust calibration method.
    return 1 / (1 + pd.np.exp(-score))

def import_scorer(path: str):
    """
    Imports a custom scoring function from a Python file.
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location("custom_scorer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.score # Assumes the function is named 'score'
