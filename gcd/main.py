def gcd(x, y):
    while x != 0:
        if x < y:
            x, y = y, x
        x %= y

    return y

if __name__ == "__main__":
    assert gcd(4, 6) == 2
    assert gcd(1680, 640) == 80
