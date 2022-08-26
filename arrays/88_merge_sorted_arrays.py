class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1) - 1
        l = m - 1
        r = n - 1

        while (r >= 0 and l >= 0):
            if (nums2[r] > nums1[l]):
                nums1[k] = nums2[r]
                k -= 1
                r -= 1
            else:
                nums1[k] = nums1[l]
                k -= 1
                l -= 1
        while(r >= 0):
            nums1[k] = nums2[r]
            r -= 1
            k -= 1
        while(l >= 0):
            nums1[k] = nums1[l]
            l -= 1
            k -= 1
        return nums1


s = Solution()
print(s.merge(nums1=[2, 0], m=1, nums2=[1], n=1))
