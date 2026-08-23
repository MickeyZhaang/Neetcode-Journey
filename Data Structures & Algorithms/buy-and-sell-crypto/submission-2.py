class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # invariance -- min prices throughout days
        lowest_price = 0
        max_profit = 0
        
        for i in range(len(prices)):
            if i == 0:
                lowest_price = prices[i]
                continue
            max_profit = max(max_profit, prices[i] - lowest_price)
            lowest_price = min(lowest_price, prices[i])
        
        return max_profit