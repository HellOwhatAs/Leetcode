#
# @lc app=leetcode.cn id=1401 lang=python3
#
# [1401] 圆和矩形是否有重叠
#

# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xb1 = x1 <= xCenter <= x2
        xb2 = x1 - radius <= xCenter <= x2 + radius
        yb1 = y1 <= yCenter <= y2
        yb2 = y1 - radius <= yCenter <= y2 + radius
        return xb1 and yb2 or xb2 and yb1 or radius ** 2 >= min(
            (xCenter - x1) ** 2 + (yCenter - y1) ** 2,
            (xCenter - x1) ** 2 + (yCenter - y2) ** 2,
            (xCenter - x2) ** 2 + (yCenter - y1) ** 2,
            (xCenter - x2) ** 2 + (yCenter - y2) ** 2
        )

# @lc code=end

print(Solution().checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
print(Solution().checkOverlap(radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))
print(Solution().checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))
print(Solution().checkOverlap(2, 8, 6, 5, 1, 10, 4))