from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profile = 0
        min_v = prices[0]
        for i in range(len(prices)):
            min_v = min(min_v,prices[i])
            profile = max(profile,max(0,prices[i]-min_v))
        return profile
        