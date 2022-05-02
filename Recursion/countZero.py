def countZero(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return 1 + countZero(n//10)
    else:
        return 0 + countZero(n//10)

n = int(input())
print(countZero(n))
