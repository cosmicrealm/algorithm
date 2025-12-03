from typing import List
from collections import Counter, defaultdict


class Solution:
    def code(self, string):
        arr = [0] * 26
        for s in string:
            arr[ord[s] - ord["a"]] += 1
        return tuple(arr)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        items = defaultdict(list)
        for s in strs:
            items[self.code(s)].append(s)
        res = list(items.values())
        return res
