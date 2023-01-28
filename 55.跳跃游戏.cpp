/*
 * @lc app=leetcode.cn id=55 lang=cpp
 *
 * [55] 跳跃游戏
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reach=0;
        for(int i=0;i<nums.size();++i){
            if(reach<i)return 0;
            reach=max(reach,i+nums[i]);
        }
        return 1;
    }
};
// @lc code=end

