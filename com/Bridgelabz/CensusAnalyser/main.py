from com.Bridgelabz.CensusAnalyser.IndiaCensusCSV import IndiaCensusCSV
from com.Bridgelabz.CensusAnalyser.IndiaStateCensus import StateCensusAnalyser

if __name__ == "__main__":
    object_of_loader = StateCensusAnalyser(
        path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCode.csv")
    print(object_of_loader.record_counter())
    object_of_loader.sort_data(sort_by='StateCode')
    object_of_loader.convert_to_json()
    object_of_loader = IndiaCensusCSV(
        path="C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.csv")
    print(object_of_loader.record_counter())
    object_of_loader.sort_data(sort_by='State')
    object_of_loader.sort_data(sort_by='Population', ascending_or_not=False)
    object_of_loader.convert_to_json()
