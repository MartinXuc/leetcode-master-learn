#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def operation(self, n: int) -> int:
        res = 0
        n_str = str(n)
        for c in n_str:
            res += int(c) ** 2
        return res
    def isHappy(self, n: int) -> bool:
        history_list = []
        while True:
            if n == 1:
                return True
            elif n in history_list:
                return False
            history_list.append(n)
            n = self.operation(n)
            
# @lc code=end

