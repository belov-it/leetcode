from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        cur = TreeNode()
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans


lr = TreeNode(4, None, None)
ll = TreeNode(3, None, None)
l1 = TreeNode(2, ll, lr)
r1 = TreeNode(5, None, None)
root = TreeNode(1, l1, r1)

s = Solution()
print(s.inorderTraversal(root))
