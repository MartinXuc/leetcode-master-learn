#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = sum(int(d) ** 2 for d in str(n))
        return False
        
# @lc code=end

