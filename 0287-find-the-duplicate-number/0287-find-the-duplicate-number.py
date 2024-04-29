class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if nums[abs(n)] < 0:
                return abs(n)
            nums[abs(n)] = -nums[abs(n)]
        

        

        