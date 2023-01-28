/*
 * @lc app=leetcode.cn id=75 lang=cpp
 *
 * [75] 颜色分类
 */

// @lc code=start
#include<vector>
#include<iostream>
#define update0 {while(firstnot0<nums.size()&&nums[firstnot0]==0)++firstnot0;}
#define update2 {while(lastnot2>-1&&nums[lastnot2]==2)--lastnot2;}
using namespace std;
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int firstnot0=0,lastnot2=nums.size()-1;
        update0
        update2
        for(int i=firstnot0;i<=lastnot2;){
            if(nums[i]==0){
                if(i>firstnot0){
                    swap(nums[firstnot0],nums[i]);
                    update0
                }
                else ++i;
            }
            else if(nums[i]==1)++i;
            else{
                if(i<lastnot2){
                    swap(nums[lastnot2],nums[i]);
                    update2
                }
            }
        }
    }
};
// @lc code=end