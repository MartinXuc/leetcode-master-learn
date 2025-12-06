#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverse_list_lr(self, s:list, l, r) -> None:
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for l in range(0, len(s), 2 * k):
            if l + k >= len(s):
                self.reverse_list_lr(s, l, len(s) - 1)
            else:
                self.reverse_list_lr(s, l, l + k - 1)
        return "".join(s)
# @lc code=end

