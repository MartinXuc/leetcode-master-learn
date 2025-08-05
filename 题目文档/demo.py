class Solution:
    def reverse_str_by_index(self, s: list, l: int, r: int) -> None:
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        i = 0 # 创建一个指针，用于遍历字符串
        while True:
            # 情况1，剩余字符数不足 k 个
            if len(s_list) - i <= k:
                self.reverse_str_by_index(s_list, i, len(s_list) - 1)
                break
            # 情况2，剩余字符数足 k 但不足 2k
            if len(s_list) - i <= 2 * k:
                self.reverse_str_by_index(s_list, i, i + k - 1)
                break
            # 其他情况
            self.reverse_str_by_index(s_list, i, i + k - 1)
            i += 2 * k
        return "".join(s_list)

if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    print(Solution().reverseStr(s, k))