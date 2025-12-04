from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            v = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i]!=v:
                    return res
            res += v
        return res