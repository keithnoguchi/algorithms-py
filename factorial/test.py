from factorial import main

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def test():
    for n in range(1, 900):
        assert main.factorial(n) == factorial(n)
