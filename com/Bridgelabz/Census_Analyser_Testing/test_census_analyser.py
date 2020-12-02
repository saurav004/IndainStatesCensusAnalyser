from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.IndiaCensusCSV import IndiaCensusCSV
from com.Bridgelabz.CensusAnalyser.IndiaStateCensus import StateCensusAnalyser
from com.Bridgelabz.CensusAnalyser.main import CSVLoader
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
obj_india_census = IndiaCensusCSV()
obj_states_analyser = StateCensusAnalyser()


def test_record_counter():
    """
    check if length of records is same or not
    """
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH, obj_india_census)
    assert csv_loader.record_counter() == 29


def test_record_counter_for_wrong_file_path():
    """
    Check if exception gets raised or not
    """
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH, obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_file_type():
    """
    Check if exception gets raised or not
    """
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE, obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_delimiter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER, obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_for_wrong_header():
    csv_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER_FILE_PATH, obj_india_census)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


def test_record_counter_csv_states():
    """
    check if length of records is same or not
    """
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_PATH_STATE_CENSUS, obj_states_analyser)
    assert csv_states_loader.record_counter() == 37


def test_record_counter_for_wrong_file_path_csv_states():
    """
    Check if exception gets raised or not
    """
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH, obj_states_analyser)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_file_type_csv_states():
    """
    Check if exception gets raised or not
    """
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE_STATE_CENSUS, obj_states_analyser)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_delimiter_csv_states():
    csv_states_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER_STATE_CENSUS, obj_states_analyser)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()


def test_record_counter_for_wrong_header_csv_states():
    csv_states_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER_FILE_PATH_STATE_CENSUS, obj_states_analyser)
    with pytest.raises(CensusAnalyserError):
        csv_states_loader.record_counter()
