#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 干掉特殊情况
        if head is None or head.next is None:
            return head
        elif head.next.next is None or head.next.next.next is None:
            A = head
            B = head.next
            A.next = B.next
            B.next = A
            return B
        # 一般情况
        # 初始化
        vH = ListNode("virtualHead", head)
        A = vH
        B = head
        C = head.next
        D = head.next.next
        # 循环
        while True:
            # 换位置的逻辑
            A.next = C
            B.next = D
            C.next = B
            # 移位前检查一下是否应该跳出循环
            if D.next is None:
                break
            elif D.next.next is None:
                A = B
                B = D
                C = D.next
                A.next = C
                B.next = None
                C.next = B
                break
            # 移位的逻辑
            A = B
            B = D
            C = B.next
            D = C.next
        return vH.next
        
        
# @lc code=end
