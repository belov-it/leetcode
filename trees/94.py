# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []

        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans


l5 = TreeNode(5)
l4 = TreeNode(4)
l3 = TreeNode(2, l4, l5)
l1 = TreeNode(3)
root = TreeNode(1, l3, l1)

s = Solution()
print(s.inorderTraversal(root))
