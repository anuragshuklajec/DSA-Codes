def selectionSort(arr,n):
    for i in range(0, n):
        index = i
        for j in range(i + 1, n):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]






n = int(input())
arr = list(map(int,input().split()[:n]))
selectionSort(arr,n)
print(*arr)


