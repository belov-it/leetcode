class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if (len(prices) == 1):
            return 0
        res = prices[1] - prices[0]
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if (prices[j]-prices[i] > res):
                    res = prices[j]-prices[i]
        if (res > 0):
            return res
        else:
            return 0


s = Solution()
print(s.maxProfit([3, 2, 1]))
