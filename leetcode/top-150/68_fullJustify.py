from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0  # 当前行的总字符长度（不含空格）

        for w in words:
            # 判断是否还能加入当前行（words + space）
            if line_len + len(line) + len(w) > maxWidth:
                # 当前行已满，需要进行两端对齐
                total_spaces = maxWidth - line_len
                gaps = len(line) - 1

                if gaps == 0:
                    # 只有一个单词的情况 → 左对齐，右边补空格
                    res.append(line[0] + " " * total_spaces)
                else:
                    # 平均分配空格
                    space_each = total_spaces // gaps
                    extra = total_spaces % gaps  # 把多余的空格从左边开始分配

                    s = ""
                    for i in range(gaps):
                        s += line[i]
                        s += " " * space_each
                        if i < extra:
                            s += " "
                    s += line[-1]  # 最后一个单词不需要加空格
                    res.append(s)

                # 清空 current line
                line = []
                line_len = 0

            # 加入当前行
            line.append(w)
            line_len += len(w)

        # 处理最后一行（左对齐）
        last = " ".join(line)
        last += " " * (maxWidth - len(last))
        res.append(last)

        return res