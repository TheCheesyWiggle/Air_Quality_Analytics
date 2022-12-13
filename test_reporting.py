import pytest
from reporting import daily_average
import utils

def test_dailyavg_1():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london harlington with no pollutant
    assert len(daily_average(data,"London Harlington", "no")) == 365

def test_dailyavg_2():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london harlington with pm10 pollutant
    assert len(daily_average(data,"London Harlington", "pm10")) == 365

def test_dailyavg_3():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london harlington with pm25 pollutant
    assert len(daily_average(data,"London Harlington", "pm25")) == 365

def test_dailyavg_4():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london marylebone with no pollutant
    assert len(daily_average(data,"London Marylebone Road", "no")) == 365

def test_dailyavg_5():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london marylebone with pm10 pollutant
    assert len(daily_average(data,"London Marylebone Road", "pm10")) == 365

def test_dailyavg_6():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london marylebone with pm25 pollutant
    assert len(daily_average(data,"London Marylebone Road", "pm25")) == 365

def test_dailyavg_7():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london N kensingnton with no pollutant
    assert len(daily_average(data,"London N Kensington", "no")) == 365

def test_dailyavg_8():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london N kensingnton with pm10 pollutant
    assert len(daily_average(data,"London N Kensington", "pm10")) == 365

def test_dailyavg_9():
    data = utils.csvs_to_dict()
    # Test the daily_avg function for london N kensingnton with pm25 pollutant
    assert len(daily_average(data,"London N Kensington", "pm25")) == 365
