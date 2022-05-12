def partition(arr,si,ei):
    pivot_ele = arr[si]
    count = 0

    for i in range(si,ei+1):
        if pivot_ele > arr[i]:
            count+=1

    pivot_index = si + count
    arr[pivot_index],arr[si] = arr[si],arr[pivot_index]
    i,j = si,ei
    while i < j:
        if (arr[i] < pivot_ele):
            i+=1
        elif arr[j] >= pivot_ele:
            j-=1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    return pivot_index


def quickSort(arr,si,ei):
    if si >= ei:
        return
    pivot_index = partition(arr,si,ei)
    quickSort(arr,si,pivot_index-1)
    quickSort(arr,pivot_index+1,ei)


arr = list(map(int,input().split()))
quickSort(arr,si = 0,ei = len(arr)-1)
print(arr)
