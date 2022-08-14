

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

    def moveZeroesBest(self, a: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = 0
        while (r <= len(a)-1):
            if (a[l] == 0 and a[r] != 0):
                a[l], a[r] = a[r], a[l]
                l += 1
                r += 1
                continue
            if (a[r] == 0):
                r += 1
                continue
            if (a[r] != 0 and a[l] != 0):
                l += 1
                continue


s = Solution()
s.moveZeroesBest([1])
