from manhattan_distance import ManhattanDistance
from basic_classifier import BasicClassifier
from classifier import Classifier
from distance import Distance
from data_reader import DataReader


def main():
    dataDirectory = "./data/"

    distance: Distance = ManhattanDistance()
    classifier: Classifier = BasicClassifier(distance)

    training = DataReader.read_observations(
        dataDirectory + "trainingsample" + ".csv")

    classifier.train(training)

    validation = DataReader.read_observations(
        dataDirectory + "validationsample" + ".csv")


if __name__ == "__main__":
    main()
