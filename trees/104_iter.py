from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class st_itrm:
    def __init__(self, TreeNode, bl):
        self.TrN = TreeNode
        self.bl = bl


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if (root == None):
            return 0
        stack = []
        cur = root
        left_h, right_h = 0, 0
        while cur or stack:
            while cur:
                stack.append(cur)
                if not fromSt:
                    left_h += 1
                cur = cur.left
            cur, isCounted = stack.pop()
            if not isCounted:
                left_h += 1
            if cur == root:
                break
            cur = cur.right
        while cur or stack:
            while cur:
                stack.append((cur, True))
                right_h += 1
                cur = cur.right
            cur, isCount = stack.pop()
            if not isCounted:
                right_h += 1
            if cur == root:
                break
            cur = cur.left
        return max(left_h, right_h)


l1 = TreeNode(9)
rl = TreeNode(15)
rr = TreeNode(7)
r1 = TreeNode(20, rl, rr)
root = TreeNode(3, l1, r1)

s = Solution()
s.maxDepth(root)
