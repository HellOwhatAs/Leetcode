#
# @lc app=leetcode.cn id=855 lang=python3
#
# [855] 考场就座
#

# @lc code=start
class ExamRoom:

    def __init__(self, n: int, init=None):
        self.seated=[] if not init else init
        self.n=n

    def seat(self) -> int:
        if not self.seated:
            self.seated.append(0)
            return 0
        elif len(self.seated)==1:
            if(self.seated[0]>self.n-1-self.seated[0]):
                self.seated.insert(0, 0)
                return 0
            else:
                self.seated.append(self.n-1)
                return self.n-1
        else:
            max_l,max_i=0,None
            for i in range(len(self.seated)-1):
                if((_:=(self.seated[i+1]-self.seated[i])//2)>max_l):
                    max_l,max_i=_,i
            if(self.seated[0]>=self.n-1-self.seated[-1]):
                if(max_l>self.seated[0]):
                    self.seated.insert(max_i+1, max_l+self.seated[max_i])
                    return self.seated[max_i+1]
                else:
                    self.seated.insert(0, 0)
                    return 0
            else:
                if(max_l>=self.n-1-self.seated[-1]):
                    self.seated.insert(max_i+1, max_l+self.seated[max_i])
                    return self.seated[max_i+1]
                else:
                    self.seated.append(self.n-1)
                    return self.n-1
            

    def leave(self, p: int) -> None:
        self.seated.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end
