from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for index, num in enumerate(nums):
            if target - num in mp:
                return [mp[target - num], index]
            mp[num] = index
        return [0, 0]


if __name__ == "__main__":
    s = Solution()
    res = s.twoSum([3, 2, 4], 6)
    print(res)
