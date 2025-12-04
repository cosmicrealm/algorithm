from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse=True)
        for i,c in enumerate(citations):
            if c >= i+1:
                h = i+1
            else:
                break
        return h
