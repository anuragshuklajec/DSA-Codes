def merge(arr1,arr2,arr):
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i+=1
            k+=1
        else:
            arr[k] = arr2[j]
            j+=1
            k+=1
    while i < len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1
    while j < len(arr2):
        arr[k] = arr2[j]
        j+=1
        k+=1


def mergeSort(arr):

    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2

    a1 = arr[:mid]
    a2 = arr[mid:]

    mergeSort(a1)
    mergeSort(a2)

    merge(a1,a2,arr)

arr = list(map(int, input().split()))
mergeSort(arr)
print(arr)
