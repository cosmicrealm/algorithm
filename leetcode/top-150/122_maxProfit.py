from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        proflie = 0
        for i in range(1,len(prices)):
            proflie += max(0,prices[i]-prices[i-1])
        return proflie