class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = dict()
        for elem in nums:
            if (elem in d):
                d[elem] += 1
            else:
                d[elem] = 1
        count = 0
        res = 0
        for key in d:
            if (d[key] > count):
                res = key
                count = d[key]
        return res


s = Solution()
print(s.majorityElement([2,  4]))
