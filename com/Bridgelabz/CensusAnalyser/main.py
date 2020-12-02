import pandas as pd
from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.IndiaCensusCSV import IndiaCensusCSV
from com.Bridgelabz.CensusAnalyser.IndiaStateCensus import StateCensusAnalyser


class CSVLoader:

    def __init__(self, path, obj):
        self.path = path
        self.obj = obj

    def record_counter(self):
        """
        Count record in file
        :return: number of records in file
        """

        try:
            col_names = repr(self.obj).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")


if __name__ == "__main__":
    CSV = CSVLoader(path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.csv", obj=IndiaCensusCSV())
    print(CSV.record_counter())
    CSV = CSVLoader(path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCode.csv", obj=StateCensusAnalyser())
    print(CSV.record_counter())
