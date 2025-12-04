from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_end = 0
        farest = 0
        for i in range(len(nums)-1):
            farest = max(farest,i+nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farest
        return jumps