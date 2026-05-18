def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

print(sum_n(10))
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
