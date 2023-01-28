/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 */

// @lc code=start
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int decreasing=nums.size()-1;
        while(decreasing>0){
            if(nums[decreasing-1]>=nums[decreasing])--decreasing;
            else break;
        }
        if(decreasing==0){
            reverse(nums.begin(),nums.end());
            return;
        }
        --decreasing;
        cout<<decreasing<<'\n';
        int ind=(lower_bound(&nums[decreasing+1],&nums[nums.size()],nums[decreasing],greater<int>())-&nums.front())-1;
        cout<<ind<<'\n';
        swap(nums[ind],nums[decreasing]);
        cout<<(&nums[decreasing+1]-&nums[0])<<' '<<(&nums[nums.size()]-&nums[0]);
        reverse(&nums[decreasing+1],&nums[nums.size()]);
    }
};
// @lc code=end