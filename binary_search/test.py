from binary_search.main import binary_search

def test():
    my_list = [1, 3, 5, 7, 9]
    assert binary_search(my_list, 5) == 2
    assert binary_search(my_list, 1) == 0
    assert binary_search(my_list, 2) is None
