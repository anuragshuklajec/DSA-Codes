class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        i, j = 0, len(height) - 1
        while i < j:
            curr = (j - i) * min(height[i],height[j])
            maxi = max(maxi,curr)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxi
        