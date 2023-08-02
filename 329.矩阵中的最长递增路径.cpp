/*
 * @lc app=leetcode.cn id=329 lang=cpp
 *
 * [329] 矩阵中的最长递增路径
 */

// @lc code=start
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<pair<int, int>>> _adjlist;
    vector<int> _cache;
    int m, n;

    vector<pair<int, int>>& adjlist(const pair<int, int>& x){
        return _adjlist[x.first * n + x.second];
    }

    int dfs(const pair<int, int>& x) {
        /////////////////////////////////////////
        if(_cache[x.first * n + x.second]) return _cache[x.first * n + x.second];
        /////////////////////////////////////////
        int ret = 0;
        for(auto& i: adjlist(x)){
            ret = max(ret, dfs({i.first, i.second}));
        }
        /////////////////////////////////////////
        _cache[x.first * n + x.second] = ret + 1;
        /////////////////////////////////////////
        return ret + 1;
    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size(), n = matrix.front().size();
        _adjlist.resize(m * n, {});
        _cache.resize(m * n, 0);

        for(int i=1; i<m; ++i){
            for(int j=0; j<n; ++j){
                if(matrix[i-1][j] > matrix[i][j]) adjlist({i, j}).push_back({i-1, j});
                else if(matrix[i-1][j] < matrix[i][j]) adjlist({i-1, j}).push_back({i, j});
            }
        }
        for(int i=0; i<m; ++i){
            for(int j=1; j<n; ++j){
                if(matrix[i][j-1] > matrix[i][j]) adjlist({i, j}).push_back({i, j-1});
                else if(matrix[i][j-1] < matrix[i][j]) adjlist({i, j-1}).push_back({i, j});
            }
        }

        int ret = 0;
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                ret = max(ret, dfs({i, j}));
            }
        }
        return ret;
    }
};
// @lc code=end

