- [力扣题目链接](https://leetcode.cn/problems/spiral-matrix-ii/)
- [代码随想录链接](https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE)

## 题目思路

首先想到的就是模拟的思路，暂时也想不出什么别的思路，猜测本题就是考察对代码的掌握程度。

经过观察，每次写完 2 条边之后，剩下的就又是一个完整的正方形，可以写成递归。不过发现这个思路下来每次写矩阵的方向是不一样的，不好统一。不过如果每次画 4 条边，则一样可以递归，而且可以做到每一层的操作是统一的。

关键点在于画出 4 条边的函数实现，定义函数：`drawEdge(const int x, const int y, const int n, int & num, vector<vector<int>>& nums)`，参数说明：

- `x,y` 起始坐标，表明下一次需要写下的位置
- `n` 正方形边长
- `num` 起始数据，表明下一次需要写下的数字
- `nums` 待操作的数组

写到这里发现可以不用递归，循环即可

## 代码实现

```python
class Solution:
    def draw_edge(self, x: int, y: int, n: int, num: int, nums: List[List[int]])-> int:
        i, j = y, x
        for j in range(x, x + n):
            nums[i][j] = num
            num += 1
        for i in range(y + 1, y + n):
            nums[i][j] = num
            num += 1
        for j in range(x + n - 2, x - 1, -1):
            nums[i][j] = num
            num += 1 
        for i in range(y + n - 2, y, -1):
            nums[i][j] = num
            num += 1
        return num

    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        x = y = 0
        num = 1
        while True:
            num = self.draw_edge(x, y, n, num, nums)
            x = y = x + 1
            n -= 2
            if n <= 0:
                break
        return nums
```

