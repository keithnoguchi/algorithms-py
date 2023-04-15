from binary_search import main

def test():
    my_list = [1, 3, 5, 7, 9]
    assert main.binary_search(my_list, 5) == 2
    assert main.binary_search(my_list, 1) == 0
    assert main.binary_search(my_list, 2) is None
