class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1,y1):
            return (x1**2 + y1**2)**(1/2)
        nums = [[distance(point[0],point[1]),point[0],point[1]] for point in points]
        heapq.heapify(nums)
        res = []
        for i in range(k):
            _,x,y = heapq.heappop(nums)
            res.append([x,y])
        return res
