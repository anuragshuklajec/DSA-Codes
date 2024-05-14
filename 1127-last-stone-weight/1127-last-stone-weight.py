class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = -1*(heapq.heappop(maxHeap))
            x = -1*(heapq.heappop(maxHeap))
            if x != y:
                heapq.heappush(maxHeap, x-y)
        if maxHeap:
            return abs(maxHeap[0])
        else:
            return 0
        