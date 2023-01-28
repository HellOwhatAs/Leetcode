/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int reader=1,writer=0;
        while(reader<nums.size()){
            if(nums[reader]!=nums[writer]){
                ++writer;
                nums[writer]=nums[reader];
            }
            else ++reader;
        }
        return writer+1;
    }
};
// @lc code=end