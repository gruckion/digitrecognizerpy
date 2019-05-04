from manhattan_distance import ManhattanDistance
from basic_classifier import BasicClassifier
from classifier import Classifier
from distance import Distance


def main():
    dataDirectory = "./data/"

    distance: Distance = ManhattanDistance()
    classifier: Classifier = BasicClassifier(distance)

    f = open(dataDirectory + "trainingsample" + ".csv", "r")


if __name__ == "__main__":
    main()
