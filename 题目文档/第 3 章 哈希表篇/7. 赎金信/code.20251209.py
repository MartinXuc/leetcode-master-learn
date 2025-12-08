#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = [0] * 26
        for c in magazine:
            magazine_letters[ord(c) - ord('a')] += 1
        for c in ransomNote:
            magazine_letters[ord(c) - ord('a')] -= 1
            if magazine_letters[ord(c) - ord('a')] < 0:
                return False
        return True
# @lc code=end

