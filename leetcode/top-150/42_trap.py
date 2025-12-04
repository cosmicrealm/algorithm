from typing import List
# 🔥 核心思路：双指针 + 局部最大值
# 	•	从两边往中间移动两个指针 left 和 right。
# 	•	同时维护两个变量：
# 	•	left_max：从左到当前位置 left 的最高柱子。
# 	•	right_max：从右到当前位置 right 的最高柱子。

# 关键结论：
# 	•	当前能接多少水取决于左右两边的最大高度的较小值。

# ⸻

# 🧠 为什么这样移动？
# 	•	如果 height[left] < height[right]：
# 	•	说明左边的高度是当前瓶颈，右边有更高的墙帮忙挡水。
# 	•	水位取决于 left_max。
# 	•	向右移动 left 指针，并更新 left_max。
# 	•	否则：
# 	•	右边的高度是当前瓶颈。
# 	•	水位取决于 right_max。
# 	•	向左移动 right 指针，并更新 right_max。

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left_max = height[0]
        right_max = height[-1]
        left = 0
        right = len(height)-1
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max,height[left])
                res += (left_max-height[left])
                left += 1
            else:
                right_max = max(right_max,height[right])
                res += (right_max-height[right])
                right -= 1
        return res