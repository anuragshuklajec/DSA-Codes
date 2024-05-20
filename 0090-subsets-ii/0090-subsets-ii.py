class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        def backtrack(i):
            if i == len(nums):
                res.append(subset[::])
                return
            
            # include ith
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

            # don't include ith
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1)
        backtrack(0)
        return res


        