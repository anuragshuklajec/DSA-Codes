def binarySearch(arr,target,start,end):
    if start > end:
        return -1

    mid = start + (end-start)//2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binarySearch(arr,target,start,mid-1)

    else:
        return binarySearch(arr,target,mid+1,end)

arr = list(map(int,input().split()))
target = int(input())
print(binarySearch(arr,target,start = 0,end=len(arr)-1))
