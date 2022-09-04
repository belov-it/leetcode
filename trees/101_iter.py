from sys import api_version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        stack = []
        if root == None:
            return True
        cur = root
        lrr = []
        rrl = []
        while cur or stack:
            while cur:
                lrr.append(cur.val)
                stack.append(cur)
                cur = cur.left
            if stack[-1] == root:
                break
            lrr.append(None)
            cur = stack.pop()
            lrr.append(cur.val)
            cur = cur.right
        cur = stack.pop()
        while cur or stack:
            while cur:
                rrl.append(cur.val)
                stack.append(cur)
                cur = cur.right
            if stack[-1] == root:
                break
            rrl.append(None)
            cur = stack.pop()
            rrl.append(cur.val)
            cur = cur.left
        return lrr == rrl


ll = TreeNode(3)
lr = TreeNode(4)
l1 = TreeNode(2, ll, lr)

rl = TreeNode(4)
rr = TreeNode(3)
r1 = TreeNode(2, rl, None)
root = TreeNode(1, l1, r1)

s = Solution()
print(s.isSymmetric(root))
