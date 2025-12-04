class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [""] * numRows
        cur = 0
        direction = -1
        for c in s:
            res[cur] += c
            if cur == 0 or cur == numRows - 1:
                direction *= -1
            cur += direction
        return "".join(res)