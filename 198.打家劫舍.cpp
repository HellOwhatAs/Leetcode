/*
 * @lc app=leetcode.cn id=198 lang=cpp
 *
 * [198] 打家劫舍
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 1) return nums.front();
        auto [dp0, dp1] = pair<int, int>({nums[0], max(nums[0], nums[1])});
        for(int i=2; i<nums.size(); ++i){
            tie(dp0, dp1) = pair<int, int>({dp1, max(dp1, dp0 + nums[i])});
        }
        return dp1;
    }
};
// @lc code=end

