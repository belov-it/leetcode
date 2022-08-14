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

    def majorityElementBest(self, a: list[int]) -> int:
        count = 1
        res = a[0]
        for i in range(1, len(a)):
            if (a[i] == res):
                count += 1
            elif (count > 0):
                count -= 1
            else:
                count += 1
                res = a[i]
        return res


s = Solution()
print(s.majorityElementBest([3, 2, 3]))
