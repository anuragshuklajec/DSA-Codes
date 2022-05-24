def longestConsecutiveSequence(arr):
    numSet = set(arr)
    longest = 0
    for n in arr:
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length +=1
            longest = max(length,longest)
    return longest


arr = list(map(int,input().split()))
print(longestConsecutiveSequence(arr))
