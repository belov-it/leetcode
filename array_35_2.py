

class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:
        def search_iter(self, nums, target, left, right):
            if (left == right):
                return right

            mid = int((right-left+1)/2)
            if (nums[mid] == target):
                return mid
            if (target < nums[mid]):
                right = mid-1
                search_iter(self, nums, target, left, right)
            else:
                left = mid+1
                search_iter(self, nums, target, left, right)
        left = 0
        right = len(nums)-1
        search_iter(self, nums, target, left, right)


'''s = Solution()
s.searchInsert([1, 2, 3], 3)'''


def searchInsert(nums: list, target: int) -> int:
    def search_iter(nums, target, left, right):
        mid = int((right+left)/2)

        if (nums[mid] == target):
            return mid
        if (left == right):
            return left+1
        if (target < nums[mid]):
            right = mid-1
            return search_iter(nums, target, left, right)
        else:
            left = mid+1
            return search_iter(nums, target, left, right)
    left = 0
    right = len(nums)-1
    return search_iter(nums, target, left, right)


print(searchInsert([1, 2, 4, 7, 9], 3))
