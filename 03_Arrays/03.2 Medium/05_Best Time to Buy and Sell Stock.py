
# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxPrice = 0
        minPrice = float("inf")
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPrice = max(maxPrice, prices[i]-minPrice)
        return maxPrice
# O(n) - O(1)
