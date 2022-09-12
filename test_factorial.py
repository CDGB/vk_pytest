def factorial(n):
    f = 1
    while n >= 1:
        f = f * n
        n = n - 1
    return f

def test_factorial():
    assert factorial(5) == 120
