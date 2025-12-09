#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class MyLinkedNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.vH = MyLinkedNode("vH")
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        return self.getNode(index).val

    def addAtHead(self, val: int) -> None:
        newNode = MyLinkedNode(val, self.vH.next)
        self.vH.next = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            preNode = self.vH
        else:
            preNode = self.getNode(index - 1)
        newNode = MyLinkedNode(val, preNode.next)
        preNode.next = newNode
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length or self.length == 0:
            return
        if index == 0:
            preNode = self.vH
        else:
            preNode = self.getNode(index - 1)
        preNode.next = preNode.next.next
        self.length -= 1
        
        
    def getNode(self, index: int) -> MyLinkedNode:
        print(f"get node, index:{index}", end="")
        cur = self.vH
        if index < 0 or index >= self.length:
            return -1
        for _ in range(index + 1):
            cur = cur.next
        return cur

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

