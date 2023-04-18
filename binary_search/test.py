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
            return mid + 1 + binary_search(a[mid+1:], item)
    else:
        return binary_search(a[:mid], item)

def test():
    my_list = []
    for i in range(0, 10000, 10):
        my_list.append(i)
    assert main.binary_search(my_list, 50) == 5
    assert main.binary_search(my_list, 10) == 1
    assert main.binary_search(my_list, 9990) == 999
    assert main.binary_search(my_list, 10000) is None

    assert main.binary_search(my_list, 50) == binary_search(my_list, 50)
    assert main.binary_search(my_list, 10) == binary_search(my_list, 10)
    assert main.binary_search(my_list, 9980) == binary_search(my_list, 9980)
    assert main.binary_search(my_list, 9990) == binary_search(my_list, 9990)
