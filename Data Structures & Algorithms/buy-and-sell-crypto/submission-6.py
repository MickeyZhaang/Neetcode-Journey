class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        minim = float("inf")

        for i in range(len(prices)):
            price = prices[i]
            minim = min(minim, price)
            dp[i] = max(dp[i-1], price - minim)

        return dp[-1]