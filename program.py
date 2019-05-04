from manhattan_distance import ManhattanDistance


def main():
    # TODO (Stephen): grab data from quandl rather than loading from file
    dataDirectory = "./data/"
    f = open(dataDirectory + "trainingsample" + ".csv", "r")

    distance = ManhattanDistance()


if __name__ == "__main__":
    main()
