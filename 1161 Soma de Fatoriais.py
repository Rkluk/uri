from math import factorial
while True:
    try:
        m, n = map(int, input().split())
        print(factorial(m) + factorial(n))
    except EOFError:
        break
