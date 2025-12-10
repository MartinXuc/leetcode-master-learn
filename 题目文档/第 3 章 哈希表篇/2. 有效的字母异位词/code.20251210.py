#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_list = [0] * 26
        for c in s:
            letter_list[ord(c) - ord('a')] += 1
        for c in t:
            letter_list[ord(c) - ord('a')] -= 1
        for count in letter_list:
            if count != 0:
                return False
        return True
# @lc code=end

