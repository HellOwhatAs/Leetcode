/*
 * @lc app=leetcode.cn id=48 lang=cpp
 *
 * [48] 旋转图像
 */

// @lc code=start
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n=matrix.size();
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                swap(matrix[i][j],matrix[j][i]);
            }
        }
        for(auto&i:matrix)reverse(i.begin(),i.end());
    }
};
// @lc code=end

