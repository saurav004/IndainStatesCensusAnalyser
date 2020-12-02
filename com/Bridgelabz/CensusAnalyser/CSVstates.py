import pandas as pd

from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.IndiaStateCensus import StateCensusAnalyser


class CSVStates:
    def __init__(self, path):
        self.path = path

    def record_counter(self):
        try:
            col_names = repr(StateCensusAnalyser()).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("file path not available")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Headers")


if __name__ == '__main__':
    CSV = CSVStates(path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCode.csv")
    print(CSV.record_counter())
