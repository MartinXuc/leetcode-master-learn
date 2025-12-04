#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建一个虚拟头结点，方便后续操作
        virtual_head = ListNode(-1, head)
        pre_ptr = virtual_head
        cur_ptr = head
        while cur_ptr is not None:
            if cur_ptr.val == val:
                pre_ptr.next = cur_ptr.next
                cur_ptr = pre_ptr.next
            else:
                pre_ptr = pre_ptr.next
                cur_ptr = pre_ptr.next
        return virtual_head.next
# @lc code=end