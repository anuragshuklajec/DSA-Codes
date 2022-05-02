def partition(a,si,ei):
    pivot = a[si]
    #find number of ele smaller than pivot
    c = 0
    for i in range(si,ei+1):
        if a[i] < pivot:
            c = c + 1
    a[si+c], a[si] = a[si], a[si+c]
    pivot_index = si+c
    i = si
    j = ei
    while i < j:
        if a[i] < pivot:
            i+=1
        elif a[j] >= pivot:
            j-=1
        else:
            a[i], a[j] = a[j], a[i]
            i+=1
            j-=1
    return pivot_index

def quickSort(arr,si,ei):
    if si >= ei:
        return

    pivot_index = partition(arr,si,ei)
    quickSort(arr,si,pivot_index - 1)
    quickSort(arr,pivot_index+1, ei)

a = list(map(int, input().split()))
quickSort(a,0, len(a) - 1)
print(a)


