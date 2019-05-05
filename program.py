from manhattan_distance import ManhattanDistance
from euclidean_distance import EuclideanDistance
from basic_classifier import BasicClassifier
from classifier import Classifier
from distance import Distance
from data_reader import DataReader
from evaluator import Evaluator


def main():
    dataDirectory = "./data/"

    distance: Distance = EuclideanDistance()
    classifier: Classifier = BasicClassifier(distance)

    training = DataReader.read_observations(
        dataDirectory + "trainingsample" + ".csv")

    classifier.train(training)

    validation = DataReader.read_observations(
        dataDirectory + "validationsample" + ".csv")

    correct = Evaluator.correct(validation, classifier)
    print("Correctly classified: ", correct)


if __name__ == "__main__":
    main()
