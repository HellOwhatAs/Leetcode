#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List
class Solution:
    def search(self,x:int,y:int,word:int)->bool:
        if self.visited[x][y]:return False
        if self.board[x][y]!=self.word[word]:return False
        word+=1
        self.visited[x][y]=True
        if word==len(self.word):return True
        for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=i<self.m and 0<=j<self.n:
                if self.search(i,j,word):return True
        self.visited[x][y]=False
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board,self.word=board,word
        self.m,self.n=len(board),len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j]==word[0]:
                    self.visited=[[False]*self.n for _ in range(self.m)]
                    if self.search(i,j,0):return True
        return False
# @lc code=end
print(Solution().exist(
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
))