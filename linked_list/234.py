from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def getLen(self, head):
            c = 0
            while head:
                c += 1
                head = head.next
            return c

        def rev(self, h):
            p, ans = None, None
            while h:
                p = h
                h = h.next
                p.next = ans
                ans = p
            return ans

        mid = int(getLen(self, head)/2)
        newHead = ListNode()
        newHead = head
        for i in range(mid):
            newHead = newHead.next
        nh = rev(self, newHead)
        for i in range(mid):
            if (nh.val != head.val):
                return False
            nh = nh.next
            head = head.next
        return True


def pr(h):
    while h:
        print(h.val)
        h = h.next


def rev(h):
    p, ans = None, None
    while h:
        p = h
        h = h.next
        p.next = ans
        ans = p
    return ans


#l4 = ListNode(1)
l3 = ListNode(2, None)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

s = Solution()
print(s.isPalindrome(l1))
