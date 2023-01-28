def mycache(dd):
    def _mycache(func):
        def ret(self,k):
            if k in dd:return dd[k]
            tmp=func(self,k)
            dd[k]=tmp
            return tmp
        return ret
    return _mycache
class Solution:
    dd={1:1}
    @mycache(dd)
    def getKthMagicNumber(self, k: int) -> int:
        ret=[self.getKthMagicNumber(k-1)]
        for i in range(k-2,0,-1):
            tmp=self.getKthMagicNumber(i)
            if tmp<ret[0]//7:break
            ret.append(tmp)
        rret=[]
        for i in ret:
            for j in (3,5,7):
                if i*j not in ret:
                    rret.append(i*j)
        return min(rret)