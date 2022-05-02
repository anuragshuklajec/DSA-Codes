def geoSum(k):
    if k == 0:
        return 1
    return 1/(2**k) + geoSum(k-1)

k = int(input())
print(format(geoSum(k),".5f"))
