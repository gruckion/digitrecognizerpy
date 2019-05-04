from abc import abstractmethod
from typing import List
from observation import Observation


class Classifier:
    """An interface a train and predict classifier"""

    @abstractmethod
    def train(self, trainingSet: List[Observation]) -> None:
        """Train the classifier on the set of observations"""
        pass

    @abstractmethod
    def predict(self, pixels: List[int]) -> str:
        """Predict the class of an input image"""
        pass
