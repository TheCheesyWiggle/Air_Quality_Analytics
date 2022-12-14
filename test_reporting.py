from reporting import daily_average, daily_median, hourly_average, monthly_average, peak_hour_date, count_missing_data
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

def test_dailymedian_1():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london harlington with no pollutant
    assert len(daily_median(data,"London Harlington", "no")) == 365

def test_dailymedian_2():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london harlington with pm10 pollutant
    assert len(daily_median(data,"London Harlington", "pm10")) == 365

def test_dailymedian_3():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london harlington with pm25 pollutant
    assert len(daily_median(data,"London Harlington", "pm25")) == 365

def test_dailymedian_4():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london marylebone with no pollutant
    assert len(daily_median(data,"London Marylebone Road", "no")) == 365

def test_dailymedian_5():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london marylebone with pm10 pollutant
    assert len(daily_median(data,"London Marylebone Road", "pm10")) == 365

def test_dailymedian_6():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london marylebone with pm25 pollutant
    assert len(daily_median(data,"London Marylebone Road", "pm25")) == 365

def test_dailymedian_7():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london N kensingnton with no pollutant
    assert len(daily_median(data,"London N Kensington", "no")) == 365

def test_dailymedian_8():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london N kensingnton with pm10 pollutant
    assert len(daily_median(data,"London N Kensington", "pm10")) == 365

def test_dailymedian_9():
    data = utils.csvs_to_dict()
    # Test the daily_median function for london N kensingnton with pm25 pollutant
    assert len(daily_median(data,"London N Kensington", "pm25")) == 365

def test_hourlyavg_1():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london harlington with no pollutant
    assert len(hourly_average(data,"London Harlington", "no")) == 24

def test_hourlyavg_2():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london harlington with pm10 pollutant
    assert len(hourly_average(data,"London Harlington", "pm10")) == 24

def test_hourlyavg_3():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london harlington with pm25 pollutant
    assert len(hourly_average(data,"London Harlington", "pm25")) == 24

def test_hourlyavg_4():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london marylebone with no pollutant
    assert len(hourly_average(data,"London Marylebone Road", "no")) == 24

def test_hourlyavg_5():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london marylebone with pm10 pollutant
    assert len(hourly_average(data,"London Marylebone Road", "pm10")) == 24

def test_hourlyavg_6():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london marylebone with pm25 pollutant
    assert len(hourly_average(data,"London Marylebone Road", "pm25")) == 24

def test_hourlyavg_7():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london N kensingnton with no pollutant
    assert len(hourly_average(data,"London N Kensington", "no")) == 24

def test_hourlyavg_8():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london N kensingnton with pm10 pollutant
    assert len(hourly_average(data,"London N Kensington", "pm10")) == 24

def test_hourlyavg_9():
    data = utils.csvs_to_dict()
    # Test the hourly_avg function for london N kensingnton with pm25 pollutant
    assert len(hourly_average(data,"London N Kensington", "pm25")) == 24

def test_monthlyavg_1():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london harlington with no pollutant
    assert len(monthly_average(data,"London Harlington", "no")) == 12

def test_monthlyavg_2():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london harlington with pm10 pollutant
    assert len(monthly_average(data,"London Harlington", "pm10")) == 12

def test_monthlyavg_3():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london harlington with pm25 pollutant
    assert len(monthly_average(data,"London Harlington", "pm25")) == 12

def test_monthlyavg_4():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london marylebone with no pollutant
    assert len(monthly_average(data,"London Marylebone Road", "no")) == 12

def test_monthlyavg_5():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london marylebone with pm10 pollutant
    assert len(monthly_average(data,"London Marylebone Road", "pm10")) == 12

def test_monthlyavg_6():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london marylebone with pm25 pollutant
    assert len(monthly_average(data,"London Marylebone Road", "pm25")) == 12

def test_monthlyavg_7():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london N kensingnton with no pollutant
    assert len(monthly_average(data,"London N Kensington", "no")) == 12

def test_monthlyavg_8():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london N kensingnton with pm10 pollutant
    assert len(monthly_average(data,"London N Kensington", "pm10")) == 12

def test_monthlyavg_9():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london N kensingnton with pm25 pollutant
    assert len(monthly_average(data,"London N Kensington", "pm25")) == 12

def test_peakhourdate_1():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london N kensingnton with pm25 pollutant
    assert type(peak_hour_date(data,"2021-09-01","London N Kensington", "pm25")) == int

def test_peakhourdate_2():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london N kensingnton with pm25 pollutant
    assert type(peak_hour_date(data,"2021-01-06","London Harlington", "pm10")) == int

def test_peakhourdate_3():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london N kensingnton with pm25 pollutant
    assert type(peak_hour_date(data,"2021-05-26","London Marylebone Road", "no")) == int

def test_countmissing_1():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london Harlington with pm25 pollutant
    assert type(count_missing_data(data,"London Harlington","no")) == int

def test_countmissing_2():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london Harlington with pm25 pollutant
    assert type(count_missing_data(data,"London Harlington","pm10")) == int

def test_countmissing_3():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london harlington with pm25 pollutant
    assert type(count_missing_data(data,"London Harlington","pm25")) == int

def test_countmissing_4():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london marylebone road with pm25 pollutant
    assert type(count_missing_data(data,"London Marylebone Road","no")) == int

def test_countmissing_5():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london marylebone road with pm25 pollutant
    assert type(count_missing_data(data,"London Marylebone Road","pm10")) == int

def test_countmissing_6():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london marylebone road with pm25 pollutant
    assert type(count_missing_data(data,"London Marylebone Road","pm25")) == int

def test_countmissing_7():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london  road withN Kensignton no pollutant
    assert type(count_missing_data(data,"London N Kensington","no")) == int

def test_countmissing_8():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london  road withN Kensignton pm10 pollutant
    assert type(count_missing_data(data,"London N Kensington","pm10")) == int

def test_countmissing_9():
    data = utils.csvs_to_dict()
    # Test the monthly_avg function for london  road withN Kensignton  pm25 pollutant
    assert type(count_missing_data(data,"London N Kensington","pm25")) == int