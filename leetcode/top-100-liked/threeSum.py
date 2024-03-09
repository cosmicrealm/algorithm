from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        num_len = len(nums) - 1
        for index, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            target = -num
            left = index + 1
            right = num_len
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < num_len and nums[left] == nums[left - 1]:
                        left += 1
                    while right > index and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] >= target:
                    right -= 1
                else:
                    left += 1
        return res
