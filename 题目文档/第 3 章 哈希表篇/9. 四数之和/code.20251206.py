#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        ans = []
        if nums[n - 4] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            return []
        for i in range(n - 3):
            # i 从第二次开始去重
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # 剪枝
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            # 继续处理
            for j in range(i + 1, n - 2):
                # j 从第二次开始去重
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                # 剪枝
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                # 继续处理
                k, l = j + 1, n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k - 1] == nums[k]:
                            k += 1
                        while k < l and nums[l + 1] == nums[l]:
                            l -= 1
        return ans
                    
# @lc code=end

