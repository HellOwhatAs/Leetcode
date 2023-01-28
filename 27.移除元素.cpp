/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(nums.empty())return 0;
        int finder=0,ender=nums.size()-1;
        while(finder<ender){
            if(nums[finder]==val){
                nums[finder]=nums[ender];
                --ender;
            }
            else ++finder;
        }
        if(nums[finder]==val)return finder;
        return finder+1;
    }
};
// @lc code=end

