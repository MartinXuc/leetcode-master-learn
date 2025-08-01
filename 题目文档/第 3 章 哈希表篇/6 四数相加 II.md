- [题目链接](https://leetcode.cn/problems/4sum-ii/)
- [代码随想录链接](https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html)

## 题目思路

显然最暴力的写法复杂度是 `n^4`，可以两两组合，变成两数之和问题，两两组合的复杂度是 `n^2`，再两数之和复杂度是 `n`，这样总体复杂度还是 `n^2`。暂时没想到更简单的写法，就先这样好了。

## 代码实现

```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        # 先将前两个数组组合
        dict12 = dict()
        dict34 = dict()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum12 = nums1[i] + nums2[j]
                sum34 = nums3[i] + nums4[j]
                if dict12.get(sum12) is None:
                    dict12[sum12] = [(i, j)]
                else:
                    dict12[sum12].append((i, j))
                if dict34.get(sum34) is None:
                    dict34[sum34] = [(i, j)]
                else:
                    dict34[sum34].append((i, j))
        # 再进行两数之和的问题
        for sum12 in dict12.keys():
            if -sum12 in dict34:
                ans += len(dict34[-sum12]) * len(dict12[sum12])
        return ans
```

## 看录后想法

思路一致，有一个可以优化的小点，就是字典存键值对的个数，保留下标对于本题其实意义不大的。

## 小结

无。