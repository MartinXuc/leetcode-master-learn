#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vH = ListNode("virtualHead", head)
        slow_ptr = vH
        fast_ptr = vH
        for _ in range(n):
            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
            else:
                return head
        while fast_ptr.next is not None:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return vH.next
# @lc code=end

