def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1

    return result

if __name__ == "__main__":
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    print("factorial(1000):", factorial(1000))
