#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or
            head.next is None or
            head.next.next is None):
            return None
        slow_ptr = head
        fast_ptr = ListNode(-1, head.next)
        while (fast_ptr.next is not None and
               fast_ptr.next.next is not None and
               slow_ptr != fast_ptr):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        # 无环退出
        if slow_ptr != fast_ptr:
            return None
        # 有环继续走
        slow_ptr = head
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return slow_ptr
# @lc code=end

