def printToN(n):
    if n == 0:
        return
    printToN(n-1)
    print(n)

n = int(input())
printToN(n)
