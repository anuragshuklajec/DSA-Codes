class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []
        

    def addNum(self, num: int) -> None:    
        if self.bigHeap and num > self.bigHeap[0]:
            heapq.heappush(self.bigHeap, num)
        else:
            heapq.heappush(self.smallHeap, -1 * num)

        if len(self.smallHeap) > len(self.bigHeap) + 1:
            heapq.heappush(self.bigHeap,- 1 * heapq.heappop(self.smallHeap))
        if len(self.bigHeap) > len(self.smallHeap) + 1:
            heapq.heappush(self.smallHeap, -1 * heapq.heappop(self.bigHeap))
        

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.bigHeap):
            return -1 * self.smallHeap[0]
        elif len(self.bigHeap) > len(self.smallHeap):
            return self.bigHeap[0]
        return (-1 * self.smallHeap[0] + self.bigHeap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()