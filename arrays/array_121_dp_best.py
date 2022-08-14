class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while (r <= len(prices)-1):
            if (prices[r] > prices[l]):
                profit = max(profit, prices[r] - prices[l])
            if (prices[r] < prices[l]):
                l = r

            r += 1
        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
