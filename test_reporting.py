import pytest
from reporting import daily_average
import utils

def test_dailyavg():
    data = utils.csvs_to_dict()
    # Test the daily_avg function
    assert len(daily_average(data,"London Harlington", "no")) == 365