class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        for i in range(len(s)):
            res += dic[s[i]]
            if i > 0 and dic[s[i]] > dic[s[i-1]]:
                res -= dic[s[i-1]]*2
                
        return res