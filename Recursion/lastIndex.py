def lastIndex(arr,x,si):
    l = len(arr)
    if si == l:
        return -1
    smallerOutput = lastIndex(arr,x,si+1)
    if smallerOutput != -1:
        return smallerOutput
    else:
        if arr[si] == x:
            return si
        else:
            return -1

arr = list(map(int,input().split()))
x = int(input())
print(lastIndex(arr,x,si=0))
