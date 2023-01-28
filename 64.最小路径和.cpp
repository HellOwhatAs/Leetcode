/*
 * @lc app=leetcode.cn id=64 lang=cpp
 *
 * [64] 最小路径和
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int m,n,dd[200][200];
    vector<vector<int>>* data;
    int dp(int x,int y){
        if(dd[x][y]!=-1)return dd[x][y];
        int ret=(*data)[x][y];
        if(x==m-1&&y==n-1);
        else if(x==m-1)ret+=dp(x,y+1);
        else if(y==n-1)ret+=dp(x+1,y);
        else ret+=min(dp(x+1,y),dp(x,y+1));
        return dd[x][y]=ret;
    }
    int minPathSum(vector<vector<int>>& grid) {
        m=grid.size();n=grid[0].size();data=&grid;
        for(int i=0;i<m;++i)for(int j=0;j<n;++j)dd[i][j]=-1;
        return dp(0,0);
    }
};
// @lc code=end

