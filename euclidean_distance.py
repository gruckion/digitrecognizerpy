from typing import List
from distance import Distance
from math import fabs
from scipy.spatial.distance import euclidean


class EuclideanDistance(Distance):
    """Distance between pixels based on Euclidean"""

    def between(self, pixels1: List[int], pixels2: List[int]) -> float:
        if (len(pixels1) != len(pixels2)):
            raise ValueError("Inconsistent image sizes.")

        return distance.euclidean(pixels1, pixels2)
