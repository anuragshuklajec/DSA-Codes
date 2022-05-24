def pairsWithDifferenceK(arr,k):
    d = {}
    for ele in arr: d[ele] = d.get(ele,0) + 1
    count = 0
    if k == 0:
        for key in d:
            if d[key] > 1:
                count+=1
        return count
    for key in d:
        if key + k in d:
            count+=1
    return count

arr = list(map(int,input().split()))
k = int(input())
print(pairsWithDifferenceK(arr,k))
