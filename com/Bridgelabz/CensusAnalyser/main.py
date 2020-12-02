import pandas as pd
# from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.IndiaCensusCSV import IndiaCensusCSV


class CSVLoader:

    def __init__(self, path):
        self.path = path

    def record_counter(self):
        """
        Count record in file
        :return: number of records in file
        """
        # try:
        col_names = repr(IndiaCensusCSV()).split(",")
        data = pd.read_csv(self.path, usecols=col_names)
        return len(data)
        # except FileNotFoundError:
            # raise CensusAnalyserError("Check file path")
        # except ValueError:
            # raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")


if __name__ == "__main__":
    x = CSVLoader(path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.csv")
    print(x.record_counter())
