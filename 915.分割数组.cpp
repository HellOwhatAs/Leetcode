/*
 * @lc app=leetcode.cn id=915 lang=cpp
 *
 * [915] 分割数组
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int *leftmax=new int[nums.size()],*rightmin=new int[nums.size()];
        leftmax[0]=nums[0];
        rightmin[nums.size()-2]=nums[nums.size()-1];
        for(int i=1;i<nums.size();++i){
            leftmax[i]=max(leftmax[i-1],nums[i]);
        }
        for(int i=nums.size()-3;i>=0;--i){
            rightmin[i]=min(rightmin[i+1],nums[i+1]);
        }
        for(int i=0;i<nums.size()-1;++i){
            if(leftmax[i]<=rightmin[i])return i+1;
        }
        return nums.size()-1;
    }
};
// @lc code=end

