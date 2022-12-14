from intelligence import find_red_pixels, find_cyan_pixels, detect_connected_components, bubble_sort, get_neighbors
import numpy as np

def test_findredpixels_1():
    assert type(find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)) == np.ndarray

def test_findcyanpixels_1():
    assert type(find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)) == np.ndarray