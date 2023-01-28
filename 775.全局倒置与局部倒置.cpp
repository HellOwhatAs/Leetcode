/*
 * @lc app=leetcode.cn id=775 lang=cpp
 *
 * [775] 全局倒置与局部倒置
 */

// @lc code=start
#include<vector>

using namespace std;
class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        int *Max=new int[nums.size()];
        Max[0]=nums[0];
        for(int i=1;i<nums.size();++i){
            Max[i]=max(Max[i-1],nums[i]);
        }
        for(int i=2;i<nums.size();++i){
            if(nums[i]<Max[i-2])return false;
        }
        return true;
    }
};
// @lc code=end

