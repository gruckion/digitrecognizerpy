from observation import Observation
from typing import List


class DataReader:
    @staticmethod
    def observation_factory(data: str) -> Observation:
        commaSeparated: List[str] = data.split(",")
        label: str = commaSeparated[0]
        pixels: List[int] = list(map(int, commaSeparated[1:]))
        return Observation(label, pixels)

    @staticmethod
    def read_observations(dataPath: str) -> List[Observation]:
        # TODO (Stephen): remove the need for this list of string
        read_file: List[str] = []
        with open(dataPath, "r") as f:
            read_file.extend(f.readlines())

        return list(map(DataReader.observation_factory, read_file[1:]))
