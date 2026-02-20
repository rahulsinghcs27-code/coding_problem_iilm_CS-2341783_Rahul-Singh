from ast import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            sellingPrice = prices[i]
            if sellingPrice > buyingPrice:
                profit = max(profit, (sellingPrice - buyingPrice))
            if buyingPrice > sellingPrice:
                buyingPrice = prices[i]
        return profit