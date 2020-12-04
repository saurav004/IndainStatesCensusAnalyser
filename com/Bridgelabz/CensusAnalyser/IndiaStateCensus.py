from com.Bridgelabz.CensusAnalyser.CSVBuilder import CSVBuilder
from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.CSVloader import CSVLoader


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
            data = CSVLoader(self.path, self).load_csv()
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")
