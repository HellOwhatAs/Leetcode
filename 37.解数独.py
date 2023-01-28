#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
from typing import List
class Solution:
    def valid(self,board:List[List[str]],tx:int,ty:int,k:str)->bool:
        for i in range(9):
            if (self.board[tx][i]==k if self.board[tx][i]!='.' else board[self.rpos[tx,i]]==k if self.rpos[tx,i]<len(board) else False):return False
            if (self.board[i][ty]==k if self.board[i][ty]!='.' else board[self.rpos[i,ty]]==k if self.rpos[i,ty]<len(board) else False):return False
        _x,_y=tx//3*3,ty//3*3
        for i in range(_x,_x+3):
            for j in range(_y,_y+3):
                if (self.board[i][j]==k if self.board[i][j]!='.' else board[self.rpos[i,j]]==k if self.rpos[i,j]<len(board) else False):
                    return False
        return True
    def func(self,decideds:List[List[str]])->List[List[str]]:
        return [i+[j] for i in decideds for j in "123456789" if self.valid(i,*self.pos[len(decideds[0])],j)]
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board=board
        self.pos=[(i,j) for i in range(9) for j in range(9) if board[i][j]=='.']
        self.rpos={i:ind for ind,i in enumerate(self.pos)}
        ret=[[str(i)] for i in range(1,10) if self.valid(board,*self.pos[0],str(i))]
        for i in range(1,len(self.pos)):
            ret=self.func(ret)
        ret=ret[0]
        for i in range(len(ret)):
            x,y=self.pos[i]
            board[x][y]=ret[i]
# @lc code=end
from pprint import pprint
s=Solution()
board=[
[".",".",".","2",".",".",".","6","3"],
["3",".",".",".",".","5","4",".","1"],
[".",".","1",".",".","3","9","8","."],
[".",".",".",".",".",".",".","9","."],
[".",".",".","5","3","8",".",".","."],
[".","3",".",".",".",".",".",".","."],
[".","2","6","3",".",".","5",".","."],
["5",".","3","7",".",".",".",".","8"],
["4","7",".",".",".","1",".",".","."]]
s.solveSudoku(board)
pprint(board)