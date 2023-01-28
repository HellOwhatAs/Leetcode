/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */

// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        for(int i=1;i<nums.size();++i)nums[i]+=nums[i-1];
        int recent_min=0,recent_ret=-100000;
        for(auto&i:nums){
            recent_ret=max(recent_ret,i-recent_min);
            recent_min=min(recent_min,i);
        }
        return recent_ret;
    }
};
// @lc code=end

