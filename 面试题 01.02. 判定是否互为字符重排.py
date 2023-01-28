class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):return False
        d={}
        for i in s1:
            if i in d:d[i]+=1
            else: d[i]=1
        for i in s2:
            if i in d:
                if d[i]==1:d.pop(i)
                else:d[i]-=1
            else:return False
        return not bool(d)


print(Solution().CheckPermutation("abc", s2 = "bad"))