def minToOne(n):
    if n == 1:
        return 0
    ans1 = minToOne(n-1)
    ans2 = 1000000
    if n % 2 == 0:
        ans2 = minToOne(n/2)
    ans3 = 1000000
    if n % 3 == 0:
        ans3 = minToOne(n/3)
    return 1+min(ans1,ans2,ans3)

n = int(input())
print(minToOne(n))
