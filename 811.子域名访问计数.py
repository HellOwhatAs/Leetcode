#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def func(self,x:str):
        n,x=int(x[:(tmp:=x.find(' '))]),x[tmp+1:]
        while True:
            self.data[x]+=n
            if (tmp:=x.find('.'))==-1:break
            x=x[tmp+1:]
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        self.data=defaultdict(lambda:0)
        for i in cpdomains:self.func(i)
        return [f"{v} {k}" for k,v in self.data.items()]
# @lc code=end
print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))