from typing import List


class ListNode:
    def __init__(self, x=0, Next=None):
        self.val = x
        self.Next = Next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = ListNode()
        fast = ListNode()
        slow = head
        fast = head
        while True:
            if (fast == None):
                return False
            fast = fast.Next
            if (fast == slow):
                return True
            fast = fast.Next
            slow = slow.Next


l1 = ListNode(1, None)
l2 = ListNode(2, l1)
s = Solution()
s.hasCycle(l2)
