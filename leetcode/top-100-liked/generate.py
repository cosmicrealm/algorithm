class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        if numRows == 1:
            return res
        for i in range(1, numRows):
            pre_list = res[-1]
            cur_list = [0] * (len(pre_list) + 1)
            for i in range(len(cur_list)):
                if i == 0 or i == len(cur_list) - 1:
                    cur_list[i] = 1
                else:
                    cur_list[i] = pre_list[i - 1] + pre_list[i]
            res.append(cur_list)
        return res
