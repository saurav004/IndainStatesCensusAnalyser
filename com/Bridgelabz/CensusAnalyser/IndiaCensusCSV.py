from com.Bridgelabz.CensusAnalyser.CSVBuilder import CSVBuilder
from com.Bridgelabz.CensusAnalyser.CSVloader import CSVLoader


class IndiaCensusCSV(CSVBuilder):
    data = None

    def __init__(self, path):
        self.path = path
        self.state = "State"
        self.population = "Population"
        self.area = "AreaInSqKm"
        self.density = "DensityPerSqKm"

    def __repr__(self):
        return self.state + "," + self.population + "," + self.density + "," + self.area

    def record_counter(self):
        IndiaCensusCSV.data = CSVLoader(self.path, self).load_csv()
        return len(IndiaCensusCSV.data)

    @staticmethod
    def sort_data(sort_by=None):
        IndiaCensusCSV.data = IndiaCensusCSV.data.sort_values(sort_by)
        print('after sorting')
        print(IndiaCensusCSV.data)
        return IndiaCensusCSV.data

    @staticmethod
    def convert_to_json():
        IndiaCensusCSV.data = IndiaCensusCSV.data.to_json()
        print('In json format')
        print(IndiaCensusCSV.data)
