def sumofdigit(n):
    assert n >= 0 and int(n) == n, "this is not a positive number"
    if n in range(0,10):
        return n
    else:
        return int(n%10) + sumofdigit(int(n/10))

print(sumofdigit(23.9))