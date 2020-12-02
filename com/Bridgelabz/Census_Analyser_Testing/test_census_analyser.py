from com.Bridgelabz.CensusAnalyser.CSVstates import CSVStates
from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.main import CSVLoader
import pytest

CENSUS_CSV_FILE_PATH = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.xls"
CENSUS_CSV_FILE_WRONG_DELIMITER = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndianStateCensusDifferentDelimiter.csv"
CENSUS_CSV_WRONG_HEADER_FILE_PATH = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData1.csv"


def test_record_counter():
    """
    check if length of records is same or not
    """
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.record_counter() == 29


def test_record_counter_for_wrong_file_path():
    """
    Check if exception gets raised or not
    """
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_file_type():
    """
    Check if exception gets raised or not
    """
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_delimiter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_header():
    csv_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_csv_states():
    """
    check if length of records is same or not
    """
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_PATH)
    assert csv_states_loader.record_counter() == 29


def test_record_counter_for_wrong_file_path_csv_states():
    """
    Check if exception gets raised or not
    """
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_file_type_csv_states():
    """
    Check if exception gets raised or not
    """
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_delimiter_csv_states():
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_header_csv_states():
    csv_states_loader = CSVStates(CENSUS_CSV_WRONG_HEADER_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()
