from abc import abstractmethod


class Distance:
    """An interface for distance for pixels."""

    @abstractmethod
    def between(self, x: int, y: int) -> float:
        """For calculating the distance between arrays of pixels
        """
        pass
