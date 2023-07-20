/*
 * @lc app=leetcode.cn id=918 lang=cpp
 *
 * [918] 环形子数组的最大和
 */

// @lc code=start
#include<vector>
#include<numeric>
using namespace std;
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        pair<int, int> dp_max = {nums[0], 1}, dp_min = {nums[0], 1};
        int ret = nums[0], min_val = nums[0], min_l = 1;
        for(int i=1; i<nums.size(); ++i){
            dp_max = max(pair<int, int>(dp_max.first + nums[i], dp_max.second + 1), pair<int, int>(nums[i], 1));
            dp_min = min(pair<int, int>(dp_min.first + nums[i], dp_min.second + 1), pair<int, int>(nums[i], 1));
        
            ret = max(ret, dp_max.first);
            if(dp_min.first < min_val) tie(min_val, min_l) = dp_min;
        }

        if(min_l < nums.size()) ret = max(ret, accumulate(nums.begin(), nums.end(), 0) - min_val);
        return ret;
    }
};
// @lc code=end

