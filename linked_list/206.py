class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        lists = []
        while head:
            lists.append(head)
            head = head.next
        if (len(lists) == 0):
            return None
        newHead = ListNode()
        cur = ListNode()
        cur = lists[len(lists)-1]
        newHead.next = cur
        for i in range(len(lists)-1, 0, -1):
            cur = lists[i]
            cur.next = lists[i-1]
        lists[0].next = None
        return newHead.next


def pr(ln):
    while ln:
        print(ln.val)
        ln = ln.next


l3 = ListNode(4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
r = ListNode(1)

s = Solution()
pr(s.reverseList(r))
