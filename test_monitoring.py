from monitoring import get_live_data_from_api_hourly, get_live_data_from_api_radar, get_live_data_pollutant_plot

def test_getlivedatahourly_1():
    #test whether the correct datatype is returned
    assert type(get_live_data_from_api_hourly()) == dict

def test_getlivedatafromradar_1():
    #test whether the correct datatype is returned
    assert type(get_live_data_from_api_radar())== tuple

def test_getlivedatapollpolt_1():
    #test whether the correct datatype is returned
    assert type(get_live_data_pollutant_plot())== dict

