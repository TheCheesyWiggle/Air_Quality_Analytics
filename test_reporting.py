import pytest
import reporting
import utils

def test_daily_avg():
    data = utils.csvs_to_dict()
    # Test the daily_avg function
    assert len(reporting.daily_average(data,"London Harlington", "no")) == 365