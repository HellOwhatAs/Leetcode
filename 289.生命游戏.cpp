/*
 * @lc app=leetcode.cn id=289 lang=cpp
 *
 * [289] 生命游戏
 */

// @lc code=start
#include<vector>
using namespace std;
#define FUNC(x,y) {int ii=x, jj=y;if(ii>=0 && ii<board.size() && jj>=0 && jj<board[i].size())sum_+=(board[ii][jj] & 1);}
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        for(int i=0;i<board.size();++i){
            for(int j=0;j<board[i].size();++j){
                int sum_=0;
                FUNC(i-1, j-1) FUNC(i-1, j) FUNC(i-1, j+1)
                FUNC(i  , j-1)              FUNC(i  , j+1)
                FUNC(i+1, j-1) FUNC(i+1, j) FUNC(i+1, j+1)
                if(sum_<2 || sum_>3)board[i][j] &= ~(1<<1);
                else if(sum_==3)board[i][j] |= (1<<1);
                else board[i][j]+=(board[i][j]<<1);
            }
        }
        for(int i=0;i<board.size();++i){
            for(int j=0;j<board[i].size();++j){
                board[i][j]>>=1;
            }
        }
    }
};
#undef FUNC
// @lc code=end

