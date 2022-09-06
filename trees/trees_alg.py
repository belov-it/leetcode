from logging.config import valid_ident
from tkinter.tix import Tree
from turtle import left


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def DFS(root: TreeNode) -> None:
    # Обход в ширину
    if (root == None):
        return
    stack = []
    stack.append(root)
    cur = root
    while stack:
        cur = stack.pop()
        print(cur.val)
        if (cur.right != None):
            stack.append(cur.right)
        if (cur.left != None):
            stack.append(cur.left)


def BFS(root: TreeNode) -> None:
    # Обход в глубину
    if (root == None):
        return
    stack = []
    stack.append(root)
    cur = root
    while stack:
        cur = stack.pop(0)
        print(cur.val)
        if (cur.right != None):
            stack.append(cur.right)
        if (cur.left != None):
            stack.append(cur.left)


# left subtreee
ll = TreeNode(1, None, None)
lr = TreeNode(5, None, None)
l = TreeNode(2, ll, lr)
# right subtree
rl = TreeNode(8, None, None)
rr = TreeNode(12, None, None)
r = TreeNode(10, rl, rr)

root = TreeNode(7, l, r)

BFS(root)
