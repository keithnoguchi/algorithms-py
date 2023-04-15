def selection_sort(array):
    new_array = []

    while len(array) > 0:
        smallest = array[0]
        smallest_index = 0

        for i in range(1, len(array)):
            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i
        new_array.append(array.pop(smallest_index))

    return new_array

if __name__ == "__main__":
    array = [5, 3, 2, 1, 4]

    print(selection_sort(array))
