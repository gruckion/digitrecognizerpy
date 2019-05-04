from abc import abstractmethod
from typing import List


class Distance:
    """An interface for distance for pixels."""

    @abstractmethod
    def between(self, pixels1: List[int], pixels2: List[int]) -> float:
        """For calculating the distance between arrays of pixels"""
        pass
