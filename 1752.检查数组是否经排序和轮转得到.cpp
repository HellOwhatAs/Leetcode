/*
 * @lc app=leetcode.cn id=1752 lang=cpp
 *
 * [1752] 检查数组是否经排序和轮转得到
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    bool check(vector<int>& nums) {
        int count=0;
        for(int i=1;i<nums.size();++i){
            if(nums[i-1]>nums[i])++count;
        }
        if(count==0)return true;
        if(count==1 && nums.front()>=nums.back())return true;
        return false;
    }
};
// @lc code=end

