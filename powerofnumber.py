def power(n,m):
    assert m > 0 and int(m) == m, "power  is not a positive number"
    if m ==1:
        return n
    else:
        return n * power(n,m-1)

print(power(94,5))