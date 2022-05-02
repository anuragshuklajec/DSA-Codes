def sumOfdigits(n):
    if n == 0:
        return 0
    return n%10 + sumOfdigits(n//10)

n = int(input())
print(sumOfdigits(n))
