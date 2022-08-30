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


def del_el(head, value):
    prev, cur = head, head
    while (cur):
        if (cur.val == value):
            prev.next = cur.next
            del(cur)
            return
        prev = cur
        cur = cur.next


l4 = ListNode(5, None)
l3 = ListNode(4, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

del_el(l1, 1)

pr(l1)
