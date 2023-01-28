/*
 * @lc app=leetcode.cn id=1822 lang=cpp
 *
 * [1822] 数组元素积的符号
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int arraySign(vector<int>& nums) {
        int ret=1;
        for(auto i:nums){
            if(i==0)return 0;
            if(i<0)ret=-ret;
        }
        return ret;
    }
};
// @lc code=end

