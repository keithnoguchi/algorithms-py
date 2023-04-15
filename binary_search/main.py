def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    assert binary_search(my_list, 5) == 2
    assert binary_search(my_list, 1) == 0
    assert binary_search(my_list, 2) == None
