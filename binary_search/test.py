import random
from binary_search import main

def binary_search(a, item):
    if len(a) == 0:
        return None
    mid = len(a) // 2
    if a[mid] == item:
        return mid
    elif a[mid] < item:
        result = binary_search(a[mid+1:], item)
        if result is None:
            return None
        else:
            return mid + binary_search(a[mid+1:], item)
    else:
        return binary_search(a[:mid], item)

def test():
    my_list = []
    for i in range(0, 1000):
        my_list.append(i)
    assert main.binary_search(my_list, 5) == 5
    assert main.binary_search(my_list, 1) == 1
    assert main.binary_search(my_list, 999) == 999
    assert main.binary_search(my_list, 1000) is None

    random.shuffle(my_list);
    assert main.binary_search(my_list, 5) == binary_search(my_list, 5)
    assert main.binary_search(my_list, 1) == binary_search(my_list, 1)
    assert main.binary_search(my_list, 998) == binary_search(my_list, 998)
    assert main.binary_search(my_list, 999) == binary_search(my_list, 999)
