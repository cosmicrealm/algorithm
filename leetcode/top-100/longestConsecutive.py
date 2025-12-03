from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        sp = set(nums)
        for num in nums:
            if num - 1 not in sp:
                cur_num = num
                cur_res = 1
                while cur_num + 1 in sp:
                    cur_num += 1
                    cur_res += 1
                res = max(res, cur_res)
        return res
