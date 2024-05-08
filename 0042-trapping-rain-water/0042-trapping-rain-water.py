class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)

        for i in range(1,len(height)):
            left[i] = max(left[i-1], height[i-1])
        print(left)

        for i in range(len(height)-2,-1,-1):
            right[i] = max(right[i+1], height[i+1])
        print(right)

        res = 0
        for i in range(len(height)):
            if min(left[i],right[i])-height[i] > 0:
                res+=min(left[i],right[i])-height[i]
        return res


        
        