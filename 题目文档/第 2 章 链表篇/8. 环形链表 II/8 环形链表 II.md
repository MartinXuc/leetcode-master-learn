- [题目链接](https://leetcode.cn/problems/linked-list-cycle-ii/)
- [代码随想录链接](https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html)

## 题目思路

如果不限制空间复杂度的话，我直接用 n 个指针去遍历就行了，不过题目肯定不是这个意思。

可以用两个指针，一个指针一次走两步，一个指针一次走一步，如果没有环的话，快指针可以访问到 None，如果有环的话，两个指针一定会相遇。但是如何确定入环的第一个点呢。

用数学方法思考一下，设时刻 t 后两个指针相遇了，快指针就走了 2t，慢指针走了 t，此时快慢指针一定是在环里相遇的，相差的 t 也一定是环的长度的整数倍，但是此时依然和进入点没关系。假设第二次相遇时走了 k 步，第二次套圈意味着快指针刚好比慢指针多走了 (k - t) 步，即圈的长度 len 是 (k - t)。

知道了圈的长度，重新将快慢指针放在 head，然后让快指针先跑 len 步，然后快慢指针一起同速前进，第一次相遇即是入圈点。

## 代码实现

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 排除和主逻辑不兼容的特殊情况
        if head is None:
            return None
        elif head.next is None:
            return None
        fast = slow = head
        # 第一次相遇
        while True:
            if fast is None:
                return None
            elif fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        # 求长度
        length = 0
        while True:
            fast = fast.next
            length += 1
            if slow is fast:
                break
        # 重设快慢指针，找入圈点
        slow = fast = head
        for _ in range(length):
            fast = fast.next
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return slow
```

## 看录后想法

并不理解代码随想录为什么要搞这么复杂，难道这种方法有其他地方的应用？目前还是觉得我的方法既简洁又清晰。

## 小结

无