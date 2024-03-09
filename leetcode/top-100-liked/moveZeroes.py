from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        cur_idx = 0
        for num in nums:
            if num != 0:
                nums[cur_idx] = num
                cur_idx += 1
        return nums
