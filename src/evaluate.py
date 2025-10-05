class WaterQualityEvaluator:
    """
    Evaluates water safety based on pH and turbidity ranges.
    """

    def __init__(self, safe_ph=(6.5, 8.5), safe_turbidity=(0.0, 1.0)):
        self.safe_ph = safe_ph
        self.safe_turbidity = safe_turbidity

    def is_safe(self, ph, turbidity):
        """
        Check if the water sample is safe based on pH and turbidity.
        Args:
            ph (float): pH level of the water sample.
            turbidity (float): Turbidity of the water sample.
        Returns:
            (bool, str): Tuple of safety status and reason.
        """
        if ph == -1:
            return False, "missing pH"
        if turbidity == -1:
            return False, "missing turbidity"
        if ph < self.safe_ph[0]:
            return False, "pH too low"
        if ph > self.safe_ph[1]:
            return False, "pH too high"
        if turbidity > self.safe_turbidity[1]:
            return False, "turbidity too high"
        return True, "Safe"

