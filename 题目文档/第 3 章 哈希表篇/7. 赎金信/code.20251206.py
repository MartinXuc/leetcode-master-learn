#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = defaultdict(int)
        for c in magazine:
            letter_count[c] += 1
        for c in ransomNote:
            if c in letter_count:
                letter_count[c] -= 1
                if letter_count[c] < 0:
                    return False
            else:
                return False
        return True
            
# @lc code=end

