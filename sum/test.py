from sum import main

def sum(a):
    total = 0
    for item in a:
        total += item

    return total

def test():
    for i in range(1, 900):
        a = list(range(0, i))
        b = list(range(0, i))
        assert main.sum(a) == sum(b)
