#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 索引：i, j, k, l
        # 下标：a, b, c, d
        n = len(nums)
        if n < 4:
            return []
        ans = []
        # 进行一个基础的排序
        nums.sort()
        
        # 最基本的剪枝
        if nums[0] + nums[1] + nums[2] + nums[3] > target:
            return []
        elif nums[n - 4] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            return []
        
        for i in range(0, n - 3):
            # 去重，重复数据中只用第一次
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 剪枝
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            elif nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            # 正常遍历
            for j in range(i + 1, n - 2):
                # 去重，重复数据中只用一次
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 剪枝
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                elif nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                # 正常遍历
                k = j + 1
                l = n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    # 去重
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
        return ans
# @lc code=end

