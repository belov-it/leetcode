class ListNode:
    def __init__(self, x=0, Next=None):
        self.val = x
        self.next = Next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA.next == None or headB == None):
            return None
        cur1 = ListNode()
        cur2 = ListNode()
        cur1 = headA
        cur2 = headB
        while (cur1 != None and cur2 != None):
            if (id(cur1.next) == id(cur2.next)):
                return cur1.next
            cur1 = cur1.next
            cur2 = cur2.next
        if (cur1.next == None):
            while (cur2 != None):
                if (id(cur1.next) == id(cur2.next)):
                    return cur1.next
                cur2 = cur2.next
        else:
            while (cur1 != None):
                if (id(cur1.next) == id(cur2.next)):
                    return cur1.next
                cur1 = cur1.next
        return None


l3 = ListNode(8)
l2 = ListNode(4, l3)
l1 = ListNode(2, l2)
r3 = ListNode()

r2 = ListNode()
r2 = l3
r1 = ListNode(1, r2)


s = Solution()
s.getIntersectionNode(l1, r1)
