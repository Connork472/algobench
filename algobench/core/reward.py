import math

def universal_reward(p: float, y: int, impact: float = 1.0) -> float:
    """
    Calculates a universal reward based on the absolute difference between prediction and outcome.
    """
    return (1 - abs(p - y)) * impact

def log_loss_reward(p: float, y: int, impact: float = 1.0) -> float:
    """
    Calculates reward using a log-loss formula, scaled by economic impact.
    """
    epsilon = 1e-8
    if y == 1:
        return -math.log(p + epsilon) * impact
    else:
        return -math.log(1 - p + epsilon) * impact
