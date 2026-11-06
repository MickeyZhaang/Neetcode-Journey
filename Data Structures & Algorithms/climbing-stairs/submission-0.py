class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * n

        for i in range(1, n):
            dp[i] = dp[i] + dp[i - 1]
        
        return dp[-1]
        