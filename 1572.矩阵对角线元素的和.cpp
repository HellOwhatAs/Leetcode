/*
 * @lc app=leetcode.cn id=1572 lang=cpp
 *
 * [1572] 矩阵对角线元素的和
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size(), ret = 0;
        for(int i=0; i<n; ++i){
            ret += mat[i][i];
            ret += mat[i][n-i-1];
        }
        if(n & 1){
            ret -= mat[n/2][n/2];
        }
        return ret;
    }
};
// @lc code=end

