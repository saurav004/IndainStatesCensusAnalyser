from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
import pandas as pd
import csv


class CSVLoader:

    def __init__(self, path, obj):
        self.path = path
        self.obj = obj

    def load_csv(self):
        try:
            col_names = repr(self.obj).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            data = self.load_csv_in_list()
            return data
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")

    def load_csv_in_list(self):
        with open(self.path, 'r') as file_open:
            file = csv.reader(file_open)
            data_as_list = list(file)
            print("before sort "+str(data_as_list))
            data_as_list.pop(0)
        return data_as_list
