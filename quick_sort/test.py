import random
from quick_sort import main

def test():
    sorted = [i for i in range(0, 100000)]
    array = sorted.copy()
    random.shuffle(array)
    assert main.quick_sort(array) == sorted
