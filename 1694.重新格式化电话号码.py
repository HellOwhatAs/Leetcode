#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        all_nums=[i for i in number if i.isdecimal()]
        all_nums2=[all_nums[i*3]+all_nums[i*3+1]+all_nums[i*3+2] for i in range(len(all_nums)//3)]
        if len(all_nums)%3==1:
            tmp=all_nums2.pop()
            all_nums2.append(tmp[:2])
            all_nums2.append(tmp[-1]+all_nums[-1])
        elif len(all_nums)%3==2:
            all_nums2.append(all_nums[-2]+all_nums[-1])
        return "-".join(all_nums2)
# @lc code=end

s=Solution()
print(s.reformatNumber("1222"))