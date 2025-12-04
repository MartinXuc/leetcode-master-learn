#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 排除特殊情况
        if head is None:
            return head
        elif head.next is None:
            return head
        elif head.next.next is None:
            temp = head.next
            head.next.next = head
            head.next = None
            return temp
        # 正常情况
        a_ptr = None
        b_ptr = head
        c_ptr = head.next
        while c_ptr is not None:
            b_ptr.next = a_ptr
            
            a_ptr = b_ptr
            b_ptr = c_ptr
            c_ptr = c_ptr.next
        b_ptr.next = a_ptr
        return b_ptr
# @lc code=end
