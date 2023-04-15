from unittest import TestCase
from main import selection_sort

class Test(TestCase):
    def test(self):
        assert selection_sort([3, 4, 5, 2, 1]) == [1, 2, 3, 4, 5]
