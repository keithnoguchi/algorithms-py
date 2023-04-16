def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    array = [5, 4, 3, 2, 1]
    assert quick_sort(array) == [1, 2, 3, 4, 5]
