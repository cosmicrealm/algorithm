class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        pre1 = 0
        pre2 = slow
        while pre1 != pre2:
            pre1 = nums[pre1]
            pre2 = nums[pre2]
        return pre1
