def firstIndex(arr,start, x):
    l = len(arr)
    if start == l:
        return -1
    if arr[start] == x:
        return start
    return firstIndex(arr,start+1,x)

arr = list(map(int, input().split()))
x =int(input())
print(firstIndex(arr,0,x))
