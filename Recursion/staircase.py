def staircase(n):
    if n < 0 :
        return 0
    if n == 0:
        return 1
    return staircase(n-1) + staircase(n-2) + staircase(n-3)

n = int(input())
print(staircase(n))
