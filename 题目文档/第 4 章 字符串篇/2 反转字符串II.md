- [题目链接](https://leetcode.cn/problems/reverse-string-ii/)
- [代码随想录链接](https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html)

## 题目思路

依然是模拟即可，注意条件判断的时候谨慎一点。由于 python 的特性，建议先将字符串转成 list 操作。

## 代码实现

```python
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
```

## 看录后想法

我的实现有一定的优化空间，情况 2 和其他情况有一定的重复，可以合并。不过感觉无伤大雅。

## 小结

将字符数组快速拼接成字符串：`"".join(s_list)`