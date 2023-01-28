#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(i.title() if len(i)>2 else i.lower() for i in title.split())
# @lc code=end

print(Solution().capitalizeTitle(title = "capiTalIze tHe titLe"))
print(Solution().capitalizeTitle(title = "First leTTeR of EACH Word"))
print(Solution().capitalizeTitle(title = "i lOve leetcode"))