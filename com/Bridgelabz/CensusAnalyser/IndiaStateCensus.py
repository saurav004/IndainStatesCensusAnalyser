from com.Bridgelabz.CensusAnalyser.CSVBuilder import CSVBuilder
from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
import pandas as pd


class StateCensusAnalyser(CSVBuilder):

    def __init__(self, path):
        self.path = path
        self.SrNo = "SrNo"
        self.StateName = "StateName"
        self.TIN = "TIN"
        self.StateCode = "StateCode"

    def __repr__(self):
        return self.SrNo + "," + self.StateName + "," + self.TIN + "," + self.StateCode

    def record_counter(self):
        try:
            col_names = self.__repr__().split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")
