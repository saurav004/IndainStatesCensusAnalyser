from com.Bridgelabz.CensusAnalyser.CSVBuilder import CSVBuilder
from com.Bridgelabz.CensusAnalyser.CSVloader import CSVLoader


class StateCensusAnalyser(CSVBuilder):
    data = None

    def __init__(self, path):
        self.path = path
        self.SrNo = "SrNo"
        self.StateName = "StateName"
        self.TIN = "TIN"
        self.StateCode = "StateCode"

    def __repr__(self):
        return self.SrNo + "," + self.StateName + "," + self.TIN + "," + self.StateCode

    def record_counter(self):
        StateCensusAnalyser.data = CSVLoader(self.path, self).load_csv()
        return len(StateCensusAnalyser.data)

    @staticmethod
    def sort_data(sort_by):
        StateCensusAnalyser.data = StateCensusAnalyser.data.sort_values(sort_by)
        print('after sorting')
        print(StateCensusAnalyser.data)
        return StateCensusAnalyser.data

    @staticmethod
    def convert_to_json():
        StateCensusAnalyser.data = StateCensusAnalyser.data.to_json()
        print('In json format')
        print(StateCensusAnalyser.data)
