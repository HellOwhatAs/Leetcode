/*
 * @lc app=leetcode.cn id=931 lang=cpp
 *
 * [931] 下降路径最小和
 */

// @lc code=start
#include<vector>
#include<climits>
using namespace std;
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for(int i=1; i<n; ++i) {
            for(int j=0; j<n; ++j) {
                int tmp = INT_MAX;
                for(int k=max(0, j-1); k<min(n, j+2); ++k) {
                    tmp = min(tmp, matrix[i-1][k]);
                }
                matrix[i][j] += tmp;
            }
        }
        int ret = matrix.back()[0];
        for(int i=1; i<n; ++i) {
            ret = min(ret, matrix.back()[i]);
        }
        return ret;
    }
};
// @lc code=end

