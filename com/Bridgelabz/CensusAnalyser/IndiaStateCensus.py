from com.Bridgelabz.CensusAnalyser.CSVBuilder import CSVBuilder
from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.CSVloader import CSVLoader
import json


class StateCensusAnalyser(CSVBuilder):
    data = []

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
            StateCensusAnalyser.data = CSVLoader(self.path, self).load_csv()
            return len(StateCensusAnalyser.data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")

    @staticmethod
    def reverse_function(e):
        return e[3]

    def sort_data_and_convert_to_json(self):
        StateCensusAnalyser.data.sort(key=self.reverse_function)
        print("in json "+json.dumps(StateCensusAnalyser.data))
