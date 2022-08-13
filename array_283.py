

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 1):
            return None
        for i in range(0, len(nums)-1):
            if (nums[i] != 0):
                continue
            for j in range(i+1, len(nums)):
                if (nums[j] == 0):
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                break


s = Solution()
s.moveZeroes([1, 0])
