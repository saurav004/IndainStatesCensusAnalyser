from com.Bridgelabz.CensusAnalyser.IndiaCensusCSV import IndiaCensusCSV
from com.Bridgelabz.CensusAnalyser.IndiaStateCensus import StateCensusAnalyser

if __name__ == "__main__":
    object_of_loader = StateCensusAnalyser(
        path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCode.csv")
    print(object_of_loader.record_counter())
    object_of_loader = IndiaCensusCSV(
        path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.csv")
    print(object_of_loader.record_counter())
