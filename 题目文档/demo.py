class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            # 若上一个元素和当前一样，没有必要继续做下去了
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 找到之后需要进行去重的逻辑，也就是重复元素不继续计算
                    while right > 0 and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
        return ans
