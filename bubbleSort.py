def bubbleSort(arr,n):
    for i in range(0,n-1):
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] == arr[j], arr[j+1]
n=int(input())
arr=list(map(int,input().split()))
bubbleSort(arr,n)
print(*arr)




