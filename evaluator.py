from typing import List
from classifier import Classifier
from basic_classifier import BasicClassifier
from observation import Observation
from statistics import mean


class Evaluator():
    @staticmethod
    def correct(validationSet: List[Observation], classifier: BasicClassifier) -> float:
        return mean([Evaluator._score(obs, classifier) for obs in validationSet])

    @staticmethod
    def _score(obs: Observation, classifier: BasicClassifier):
        score = 1.0 if classifier.predict(obs.pixels) == obs.label else 0
        print("score: ", score)
        return score
