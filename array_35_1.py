class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = (l + r)//2
            if (nums[mid] == target):
                return mid
            if (target < nums[mid]):
                r = mid - 1
            else:
                l = mid + 1
        if (nums[mid] > target):
            return mid
        return l


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 7))
