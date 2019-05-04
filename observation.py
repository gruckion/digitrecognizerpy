from typing import List


class Observation:
    """Observation model for pixels vector and model label"""

    def __init__(self, label: str, pixels: List[int]) -> None:
        """Initialise the Observation model"""
        self.label = label
        self.pixels = pixels
