

class Solution:
    def sortArrayByParity(self, a: list[int]) -> list[int]:
        n = len(a)
        l = 0
        r = n - 1
        while(r > l):
            if (a[l] % 2 != 0 and a[r] % 2 == 0):
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
            else:
                l += 1
        return a


s = Solution()
print(s.sortArrayByParity([1, 0, 3]))
