def minSquareToRepresent(n):
    if n == 0:
        return 0
    ans = 10000
    i = 1
    while i*i <= n:
        currAns = 1 + minSquareToRepresent(n-i*i)
        ans = min(ans,currAns)
        i+=1
    return ans

n = int(input())
print(minSquareToRepresent(n))
