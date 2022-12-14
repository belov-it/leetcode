class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, ans = None, head
        while head:
            ans = head
            head = head.next
            ans.next = p
            p = ans
        return ans


def pr(ln):
    while ln:
        print(ln.val)
        ln = ln.next


l3 = ListNode(4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
r = l1
r = r.next


s = Solution()
pr(s.reverseList(l1))
