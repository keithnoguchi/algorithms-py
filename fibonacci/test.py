from fibonacci import main

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def test():
    for n in range(0, 30):
        assert main.fibonacci(n) == fibonacci(n)
