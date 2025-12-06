# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        lenA, lenB = 1, 1
        ptrA, ptrB = headA, headB
        while ptrA.next is not None:
            ptrA = ptrA.next
            lenA += 1
        while ptrB.next is not None:
            ptrB = ptrB.next
            lenB += 1
        if ptrA != ptrB:
            return None
        if lenA < lenB:
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA
        ptrA, ptrB = headA, headB
        for _ in range(lenA - lenB):
            ptrA = ptrA.next
        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        return ptrA