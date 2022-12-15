from utils import maxvalue, meannvalue, minvalue, countvalue, sumvalues

def test_sumvalues_1():
    # tests for one list 
    assert sumvalues([1,3,5,3,24,5]) == 41

def test_sumvalues_2():
    # tests correct datatype is returned
    assert type(sumvalues([1,2,34,23,24,3])) == int

def test_maxvalue_1():
    # tests one list
    assert maxvalue([1,3,5,3,24,5]) == 24

def test_maxvalue_2():
    # tests that the correct datatype is returned
    assert type(maxvalue([23,453,432,23,3])) == int

def test_minvalue_1():
    # tests for one list
    assert minvalue([1,3,5,3,24,5]) == 1

def test_minvalue_2():
    #tests that the correct datatype is returned
    assert type(minvalue([23,4,23,55,63,3]))== float

def test_meanvalue_1():
    # tests for one list
    assert meannvalue([1,2,3,4,5])==3

def test_meanvalue_2():
    # tests that the datatype is correct
    assert type(meannvalue([1,2,3,4,5]))==float

def test_countvalue_1():
    # tests string
    assert countvalue([1,2,3,4,1,1,1,1,2,3,4],1)==5

def test_countvalue_2():
    #tests integer
    assert countvalue(["No data",1,3,23,"No data",3,4,5,"No data"],"No data")
