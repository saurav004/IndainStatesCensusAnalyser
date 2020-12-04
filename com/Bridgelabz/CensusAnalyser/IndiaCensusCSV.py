from com.Bridgelabz.CensusAnalyser.CSVBuilder import CSVBuilder
from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.CSVloader import CSVLoader


class IndiaCensusCSV(CSVBuilder):

    def __init__(self, path):
        self.path = path
        self.state = "State"
        self.population = "Population"
        self.area = "AreaInSqKm"
        self.density = "DensityPerSqKm"

    def __repr__(self):
        return self.state + "," + self.population + "," + self.density + "," + self.area

    def record_counter(self):
        try:
            data = CSVLoader(self.path, self).load_csv()
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")
