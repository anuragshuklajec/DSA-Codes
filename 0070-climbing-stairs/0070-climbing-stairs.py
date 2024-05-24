class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        def solve(n):
            if dp[n] != -1:
                return dp[n]
            if n < 0:
                return 0
            if n == 0:
                return 1
            dp[n] = solve(n-1) + solve(n-2) 
            return dp[n]
        return solve(n)



        
    

        
        