import math

def minSquareToRepresent(n,dp):
    if n == 0:
        return 0
    ans = 10000
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        newCheckValue = n-(i**2)
        if dp[newCheckValue] == -1:
            smallAns = minSquareToRepresent(newCheckValue,dp)
            dp[newCheckValue] = smallAns
            currAns = 1 + smallAns
        else:
            currAns = 1 + dp[newCheckValue]
        ans = min(ans,currAns)
    return ans

n = int(input())
dp = [-1 for i in range(n+1)]
print(minSquareToRepresent(n,dp))
