class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        # [7, 6, 4, 10, 11]
        # min_price = 7
        max_profit = 0
        # always 0 at beginning

        for p in prices[1:]:
            # we start at 6
            min_price = min(min_price, p)
            # min_price = min(7, 6) = 6 == 4
            profit = p - min_price
            # 10 - 4 = 6
            # profit = 11 - 4 = 7

            max_profit = max(max_profit, profit)
            # = max(6, 7)
        return max_profit



        