def sum(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + sum(a[1:])

if __name__ == "__main__":
    assert sum([]) == 0
    assert sum([1]) == 1
    assert sum([1, 2]) == 3
