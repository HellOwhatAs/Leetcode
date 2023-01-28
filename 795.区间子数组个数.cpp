/*
 * @lc app=leetcode.cn id=795 lang=cpp
 *
 * [795] 区间子数组个数
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int ret=0, valid=-1, forbid=-1;
        for(int i=0;i<nums.size();++i){
            if(left<=nums[i] && nums[i]<=right)valid=i;
            else if(nums[i]>right)forbid=i;
            ret+=max(0,valid-forbid);
        }
        return ret;
    }
};
// @lc code=end

