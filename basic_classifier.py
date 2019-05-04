import sys
from classifier import Classifier
from typing import List
from distance import Distance
from observation import Observation


class BasicClassifier(Classifier):
    def __init__(self, distance: Distance) -> None:
        self.distance = distance

    def train(self, trainingSet: List[Observation]) -> None:
        self.data = trainingSet

    def predict(self, pixels: List[int]) -> str:
        currentBest: Observation
        shortest = sys.float_info.max

        for obs in self.data:
            dist = self.distance.between(obs.pixels, pixels)
            if (dist < shortest):
                shortest = dist
                currentBest = obs

        return currentBest.label
