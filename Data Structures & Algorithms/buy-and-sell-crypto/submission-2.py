class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxP = 0

        for i in range(1, len(prices)):
            if prices[i] - buy > maxP:
                maxP = prices[i] - buy
            buy = min(buy, prices[i])
            
        return maxP
                   


        