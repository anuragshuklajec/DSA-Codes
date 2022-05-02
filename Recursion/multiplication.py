def multiplication(n,m):
    if m==1:
        return n
    return n + multiplication(n,m-1)

n,m = map(int,input().split())
print(multiplication(n,m))
