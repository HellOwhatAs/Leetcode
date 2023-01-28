#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
from typing import List,Iterable,Dict,Any,Tuple
from collections import defaultdict
def iter2dict(x:Iterable[str])->Dict[str,int]:
    ret=defaultdict(lambda *args:0)
    for i in x:
        if i!='.':ret[i]+=1
    return ret
def listslide(x:List[List[Any]],lt:Tuple[int,int],rb:Tuple[int,int])->List[List[Any]]:
    return [x[i][lt[0]:rb[0]] for i in range(lt[1],rb[1])]
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            tmp=iter2dict(i).values()
            if(tmp and max(tmp)>1):return False
        for i in range(9):
            tmp=iter2dict(
                j[i] for j in board
            ).values()
            if(tmp and max(tmp)>1):return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                tmp=iter2dict(
                    sum(listslide(board,(i,j),(i+3,j+3)),[])
                ).values()
                if(tmp and max(tmp)>1):return False
        return True
# @lc code=end