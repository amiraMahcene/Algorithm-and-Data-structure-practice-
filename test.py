def fab(n):
    if n == 0 or n == 1:
        return n
    else:
        return fab(n-2) + fab(n-1)

print(fab(5))
