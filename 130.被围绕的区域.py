#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from typing import List
class Solution:
    def dfs(self,x:int,y:int):
        self.board[x][y]=None
        for i,j in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=i<len(self.board) and 0<=j<len(self.board[0]) and self.board[i][j]=='O':
                self.dfs(i,j)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board=board
        for i in range(len(board)):
            if board[i][0]=='O':self.dfs(i,0)
            if board[i][-1]=='O':self.dfs(i,len(board[0])-1)
        for i in range(len(board[0])):
            if board[0][i]=='O':self.dfs(0,i)
            if board[-1][i]=='O':self.dfs(len(board)-1,i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':board[i][j]='X'
                elif board[i][j]==None:board[i][j]='O'
# @lc code=end

