def checkSortedList(arr,start):
    l = len(arr)
    if start == l - 1 or start == l:
        return True
    if arr[start] > arr[start+1]:
        return False
    return checkSortedList(arr,start+1)

arr = list(map(int,input().split()))
print(checkSortedList(arr,start=0))
