

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}

        for sym in s:
            if stack:
                last = stack[-1]
                if (hash[last] > 0 and (hash[last] + hash[sym] == 0)):
                    stack.pop()
                else:
                    stack.append(sym)
            else:
                stack.append(sym)
        if stack:
            return False
        return True


s = Solution()
s.isValid("([)]")
