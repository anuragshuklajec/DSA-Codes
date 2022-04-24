def binarySearch(arr,x,start,end):
    if start > end:
        return -1
    mid = end + (start - end) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearch(arr,x,start,mid-1)
    else:
        return binarySearch(arr,x,mid+1,end)


arr =list(map(int,input().split()))
x = int(input())
print(binarySearch(arr, x, start=0, end=len(arr)-1))
