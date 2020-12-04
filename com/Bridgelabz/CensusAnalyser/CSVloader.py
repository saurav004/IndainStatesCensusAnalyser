from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
import pandas as pd


class CSVLoader:

    def __init__(self, path, obj):
        self.path = path
        self.obj = obj

    def load_csv(self):
        try:
            col_names = repr(self.obj).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return data
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")
