from com.Bridgelabz.CensusAnalyser.CensusAnalysisErrors import CensusAnalyserError
from com.Bridgelabz.CensusAnalyser.main import CSVLoader
import pytest

CENSUS_CSV_FILE_PATH = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "C:/Users/Saurabh/PycharmProjects/IndianStatesCensusAnalyser/data/IndiaStateCensusData.xls"


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
