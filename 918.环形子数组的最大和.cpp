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
        vector<pair<int, int>> dp_max = {{nums[0], 1}}, dp_min = {{nums[0], 1}};
        for(int i=1; i<nums.size(); ++i){
            dp_max.push_back(max(pair<int, int>(dp_max.back().first + nums[i], dp_max.back().second + 1), pair<int, int>(nums[i], 1)));
            dp_min.push_back(min(pair<int, int>(dp_min.back().first + nums[i], dp_min.back().second + 1), pair<int, int>(nums[i], 1)));
        }
        int ret = (*max_element(dp_max.begin(), dp_max.end())).first;
        auto& [min_val, min_l] = *min_element(dp_min.begin(), dp_min.end());
        if(min_l < nums.size()) ret = max(ret, accumulate(nums.begin(), nums.end(), 0) - min_val);
        return ret;
    }
};
// @lc code=end

