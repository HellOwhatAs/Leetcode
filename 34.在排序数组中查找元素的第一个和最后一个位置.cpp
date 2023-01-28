/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */

// @lc code=start
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.empty()||nums[0]>target||nums[nums.size()-1]<target)return {-1,-1};
        auto a=lower_bound(nums.begin(),nums.end(),target);
        if(*a!=target)return {-1,-1};
        int ra=a-nums.begin(),rb=upper_bound(nums.begin(),nums.end(),target)-nums.begin()-1;
        return {ra,rb};
    }
};
// @lc code=end