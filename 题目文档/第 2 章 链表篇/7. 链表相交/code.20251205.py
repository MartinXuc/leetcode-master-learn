# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLinkedListLen(self, head: ListNode):
        if head is None:
            return 0
        cur_ptr = head
        ans = 1
        while cur_ptr.next is not None:
            cur_ptr = cur_ptr.next
            ans += 1
        return ans
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLinkedListLen(headA)
        lenB = self.getLinkedListLen(headB)
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        a_ptr = headA
        b_ptr = headB
        for _ in range(lenA - lenB):
            a_ptr = a_ptr.next
        while a_ptr != b_ptr:
            if a_ptr is None:
                return None
            a_ptr = a_ptr.next
            b_ptr = b_ptr.next
        return a_ptr