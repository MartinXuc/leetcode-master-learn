#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_list = [0] * 26
        for c in s:
            letters_list[ord(c) - ord("a")] += 1
        for c in t:
            letters_list[ord(c) - ord("a")] -= 1
        for i in letters_list:
            if i != 0:
                return False
        else:
            return True
# @lc code=end

