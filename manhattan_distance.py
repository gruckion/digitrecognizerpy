from typing import List
from distance import Distance
from math import fabs


class ManhattanDistance(Distance):
    """Distance between pixels based on the manhattan algorithm"""

    def between(self, pixels1: List[int], pixels2: List[int]) -> float:
        if (len(pixels1) != len(pixels2)):
            raise ValueError("Inconsistent image sizes.")

        distance: float = 0

        for i, (pixel1, pixel2) in enumerate(zip(pixels1, pixels2)):
            distance += fabs(pixel1 - pixel2)

        return distance
