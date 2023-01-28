/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
// [-1,0,1,2,-1,-4,-2,-3,3,0,4]
#include<vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ret;
        int tmp,l=nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<l-2&&nums[i]<=0;++i){
            if(i>0&&nums[i]==nums[i-1])continue;
            int j=i+1,k=l-1;
            while(j<k){
                if(nums[i]+nums[j]+nums[k]==0){
                    ret.push_back({nums[i],nums[j],nums[k]});
                    tmp=nums[j];
                    while(j<k&&nums[j]==tmp)++j;
                }
                else if(nums[i]+nums[j]+nums[k]>0){
                    tmp=nums[k];
                    while(k>j&&nums[k]==tmp)--k;
                }
                else {
                    tmp=nums[j];
                    while(j<k&&nums[j]==tmp)++j;
                }
            }
        }
        return ret;
    }
};
// @lc code=end

