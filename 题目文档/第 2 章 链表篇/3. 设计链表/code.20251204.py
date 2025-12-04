#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start


class LinkedNode:
    def __init__(self, val: int = None, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = LinkedNode()
        self.len = 0

    def get(self, index: int) -> int:
        cur_ptr = self._get_node(index)
        return -1 if cur_ptr is None else cur_ptr.val

    def addAtHead(self, val: int) -> None:
        new_node = LinkedNode(val, self.head.next)
        self.head.next = new_node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        cur_ptr = self._get_node(self.len - 1) if self.len > 0 else self.head
        new_node = LinkedNode(val)
        cur_ptr.next = new_node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        cur_ptr = self._get_node(index - 1) if index != 0 else self.head
        new_node = LinkedNode(val, cur_ptr.next)
        cur_ptr.next = new_node
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len or index < 0:
            return
        cur_ptr = self._get_node(index - 1) if index != 0 else self.head
        cur_ptr.next = cur_ptr.next.next
        self.len -= 1

    def _get_node(self, index) -> LinkedNode:
        if index >= self.len or index < 0:
            return None
        cur_ptr: LinkedNode = self.head.next
        for _ in range(index):
            cur_ptr = cur_ptr.next
        return cur_ptr


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

