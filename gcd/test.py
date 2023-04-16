from gcd import main

def gcd(x, y):
    if x < y:
        x, y = y, x
    x %= y
    if x == 0:
        return y
    else:
        return gcd(x, y)

def test():
    for x in range(1, 1000):
        for y in range(1, 1000):
            assert main.gcd(x, y) == gcd(x, y)
