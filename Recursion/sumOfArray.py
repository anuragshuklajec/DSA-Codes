def sumOfArray(arr,start):
    l = len(arr)
    if start == l:
        return 0
    return arr[start] + sumOfArray(arr,start+1)


arr = list(map(int, input().split()))
print(sumOfArray(arr,0))
