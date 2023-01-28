/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
#include<unordered_map>
#include<algorithm>
#include<iostream>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> dict;
        for(int i=0;i<nums.size();++i){
            if(dict.count(nums[i])){
                return {dict[nums[i]],i};
            }
            else{
                dict[target-nums[i]]=i;
            }
        }
        return {};
    }
};
// @lc code=end

