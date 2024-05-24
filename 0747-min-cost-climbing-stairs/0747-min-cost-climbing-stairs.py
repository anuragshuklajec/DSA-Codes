from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        amount = [0]
        dp = [-1 for i in range(len(cost)+1)]
        def solve(n):
            if dp[n] != -1:
                return dp[n]
            if n < 2:
                return cost[n]
            dp[n] = cost[n] + min(solve(n-1),solve(n-2))
            return dp[n]
        length = len(cost)

        return min(solve(length-1), solve(length-2))

