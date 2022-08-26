
from hashlib import new


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pr_list(Node):
    cur = ListNode()
    cur = Node
    while (cur != None):
        print(cur.val)
        cur = cur.next


class Solution:

    def mergeTwoLists(self, a: ListNode, b: ListNode) -> ListNode:

        newNode = ListNode()
        cur = ListNode()
        newNode.next = cur

        while(a != None and b != None):
            if (a.val < b.val):

                cur.next = a
                cur = a
                a = a.next
            else:

                cur.next = b
                cur = b
                b = b.next
        if (a == None):
            cur.next = b
        else:
            cur.next = a
        return newNode.next.next


l3 = ListNode(4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
r3 = ListNode(4)
r2 = ListNode(3, r3)
r1 = ListNode(1, r2)

s = Solution()
pr_list(s.mergeTwoLists(l1, r1))
