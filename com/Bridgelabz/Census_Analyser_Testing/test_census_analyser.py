from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.IndiaCensusCSV import IndiaCensusCSV
from com.Bridgelabz.CensusAnalyser.IndiaStateCensus import StateCensusAnalyser
import pytest

CENSUS_CSV_FILE_PATH = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.xls"
CENSUS_CSV_FILE_WRONG_DELIMITER = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndianStateCensusDifferentDelimiter.csv"
CENSUS_CSV_WRONG_HEADER_FILE_PATH = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData1.csv"
CENSUS_CSV_FILE_PATH_STATE_CENSUS = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCode.csv"
CENSUS_CSV_FILE_WRONG_TYPE_STATE_CENSUS = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCode.xls"
CENSUS_CSV_FILE_WRONG_DELIMITER_STATE_CENSUS = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCodeDifferentDelimiter.csv"
CENSUS_CSV_WRONG_HEADER_FILE_PATH_STATE_CENSUS = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCode1.csv"


def test_record_counter():
    """
    check if length of records is same or not
    """
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_PATH)
    assert csv_loader.record_counter() == 29


def test_record_counter_for_wrong_file_path():
    """
    Check if exception gets raised or not
    """
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_file_type():
    """
    Check if exception gets raised or not
    """
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_delimiter():
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_header():
    csv_loader = IndiaCensusCSV(CENSUS_CSV_WRONG_HEADER_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_given_csv_when_sorted_should_sort_correctly():
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_PATH)
    data = csv_loader.sort_data(sort_by='State')
    assert data.iloc[-1]['State'] == 'West Bengal' and data.iloc[0]['State'] == 'Andhra Pradesh'


def test_given_csv_when_sorted_should_sort_correctly_by_population():
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_PATH)
    data = csv_loader.sort_data(sort_by='Population', ascending_or_not=False)
    assert data.iloc[0]['State'] == 'Uttar Pradesh' and data.iloc[-1]['State'] == 'Sikkim'


def test_given_csv_when_sorted_should_sort_correctly_by_population_density():
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_PATH)
    data = csv_loader.sort_data(sort_by='DensityPerSqKm', ascending_or_not=False)
    assert data.iloc[0]['State'] == 'Bihar' and data.iloc[-1]['State'] == 'Arunachal Pradesh'


def test_given_csv_when_sorted_should_sort_correctly_by_area():
    csv_loader = IndiaCensusCSV(CENSUS_CSV_FILE_PATH)
    data = csv_loader.sort_data(sort_by='AreaInSqKm', ascending_or_not=False)
    assert data.iloc[0]['State'] == 'Rajasthan' and data.iloc[-1]['State'] == 'Goa'


def test_record_counter_csv_states():
    """
    check if length of records is same or not
    """
    csv_states_loader = StateCensusAnalyser(CENSUS_CSV_FILE_PATH_STATE_CENSUS)
    assert csv_states_loader.record_counter() == 37


def test_record_counter_for_wrong_file_path_csv_states():
    """
    Check if exception gets raised or not
    """
    csv_states_loader = StateCensusAnalyser(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_file_type_csv_states():
    """
    Check if exception gets raised or not
    """
    csv_states_loader = StateCensusAnalyser(CENSUS_CSV_FILE_WRONG_TYPE_STATE_CENSUS)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_delimiter_csv_states():
    csv_states_loader = StateCensusAnalyser(CENSUS_CSV_FILE_WRONG_DELIMITER_STATE_CENSUS)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_header_csv_states():
    csv_states_loader = StateCensusAnalyser(CENSUS_CSV_WRONG_HEADER_FILE_PATH_STATE_CENSUS)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_given_csv_when_sorted_should_sort_correctly_for_state():
    csv_loader = StateCensusAnalyser(CENSUS_CSV_FILE_PATH_STATE_CENSUS)
    data = csv_loader.sort_data(sort_by='StateCode')
    assert data.iloc[-1]['StateCode'] == 'WB' and data.iloc[0]['StateCode'] == 'AD'
