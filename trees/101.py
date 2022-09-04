# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.depth = []
        self.i = 0

    def isSym(self, l, r):
        if (l == None and r == None):
            return True
        if (l == None or r == None):
            return False
        return (l.val == r.val and self.isSym(l.left, r.right) and self.isSym(l.right, r.left))

    def isSymmetric(self, root: TreeNode) -> bool:
        if (root == None):
            return True
        return self.isSym(root.left, root.right)

    def DFS(self, root: TreeNode) -> None:
        if (root == None):
            self.depth.append(self.i)
            self.i -= 1
            return
        print(root.val)
        self.i += 1
        self.DFS(root.left)
        self.DFS(root.right)

    def maxD(self, root) -> int:
        if (root == None):
            return 0
        return max(self.maxD(root.left), self.maxD(root.right))+1


l3 = TreeNode(3)
l2 = TreeNode(4)
l1 = TreeNode(2)

r2 = TreeNode(4)
r3 = TreeNode(3)
r1 = TreeNode(2, r2, r3)
root = TreeNode(1, l1, r1)

s = Solution()


print(s.maxD(root))
