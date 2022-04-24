def pow(n,x):
    if x == 0:
        return 1
    return n * pow(n, x-1)

n,x = map(int,input().split())
print(pow(n,x))
