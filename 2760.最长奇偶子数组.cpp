/*
 * @lc app=leetcode.cn id=2760 lang=cpp
 *
 * [2760] 最长奇偶子数组
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int longestAlternatingSubarray(vector<int>& nums, int threshold) {
        vector<int> dp(nums.size());
        dp[0] = nums[0] <= threshold;
        for(int i=1; i<nums.size(); ++i){
            if(nums[i] > threshold) dp[i] = 0;
            else if((nums[i] & 1) == (nums[i-1] & 1)) dp[i] = 1;
            else dp[i] = dp[i-1] + 1;
        }
        for(int i=0; i<dp.size(); ++i){
            if(dp[i]) dp[i] -= nums[i - dp[i] + 1] % 2;
        }
        return *max_element(dp.begin(), dp.end());
    }
};
// @lc code=end

