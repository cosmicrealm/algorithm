class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        flag = False
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i]!=" ":
                flag = True
            if flag:
                if s[i] != " ":
                    res += 1
                else:
                    break
        return res
    
    def lengthOfLastWord1(self, s: str) -> int:
        i = len(s) - 1

        # 1. 去掉末尾空格
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # 2. 数最后一个单词的长度
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
