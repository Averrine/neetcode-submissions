class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        #[10, 1, 5, 6, 7, 1]
        # min = 10, 1, 1, 1, 1
        # max = 0, 4, 5, 6, 0 
        # profit = 4, 5 , 6, 6

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit