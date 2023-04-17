def fibonacci(n):
    a, b = 1, 1
    for _ in range(0, n):
        a, b = a + b, a
    return b

if __name__ == "__main__":
    assert fibonacci(0) == 1
    assert fibonacci(1) == 1
    assert fibonacci(2) == 2
    assert fibonacci(3) == 3
    assert fibonacci(4) == 5
    assert fibonacci(5) == 8
    print(fibonacci(100))
