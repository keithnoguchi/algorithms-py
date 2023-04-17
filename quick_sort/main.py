from random import random, shuffle

def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = int(random() * len(array))
    array[0], array[pivot] = array[pivot], array[0]
    pivot = 0
    for i, item in enumerate(array[1:]):
        if item < array[0]:
            pivot += 1
            array[pivot], array[i+1] = array[i+1], array[pivot]

    array[0], array[pivot] = array[pivot], array[0]
    # The following code doesn't work because slice in python is not in-place.
    # quick_sort(array[:pivot])
    # quick_sort(array[pivot+1:])
    return quick_sort(array[:pivot]) + [array[pivot]] + quick_sort(array[pivot+1:])

if __name__ == "__main__":
    want = [i for i in range(0, 1000000)]
    shuffled = want[:]
    shuffle(shuffled)
    assert quick_sort(shuffled) == want
