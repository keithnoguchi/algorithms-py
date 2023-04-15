from unittest import TestCase
from main import binary_search

class Testing(TestCase):
    def test(self):
        my_list = [1, 3, 5, 7, 9]
        assert binary_search(my_list, 5) == 2
        assert binary_search(my_list, 1) == 0
        assert binary_search(my_list, 2) == None
