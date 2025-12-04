from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        prefix_left = [1]*len(nums)
        prefix_right = [1]*len(nums)
        for i in range(1,n):
            prefix_left[i] = prefix_left[i-1] * nums[i-1]
        for j in range(n-2,-1,-1):
            prefix_right[j] = prefix_right[j+1] * nums[j+1]
        for l,r in zip(prefix_left,prefix_right):
            res.append(l*r)
        return res
        