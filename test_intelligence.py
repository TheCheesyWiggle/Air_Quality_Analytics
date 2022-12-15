from intelligence import find_red_pixels, find_cyan_pixels, detect_connected_components, bubble_sort, get_neighbors
import numpy as np

def test_findredpixels_1():
    assert type(find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)) == np.ndarray

def test_findcyanpixels_1():
    assert type(find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50)) == np.ndarray

def test_detectconnectedcomponents_1():
    assert find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50) != detect_connected_components(find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50))

def test_detectconnectedcomponents_2():
    assert find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50) != detect_connected_components(find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50))

def test_bubblesort_1():
    assert [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9] == bubble_sort({"1":5,"2":3,"3":4,"4":6,"5":1,"6":2,"7":9,"8":8,"9":7})
