/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size(), ret = 0;
        vector<int> left_max(n), right_max(n);
        left_max.front() = height.front();
        right_max.back() = height.back();
        for(int i=1; i<n; ++i){
            left_max[i] = max(left_max[i-1], height[i]);
            right_max[n-i-1] = max(right_max[n-i], height[n-i-1]);
        }
        for(int i=0; i<n; ++i){
            ret += min(left_max[i], right_max[i]) - height[i];
        }
        return ret;
    }
};
// @lc code=end

