/*
 * @lc app=leetcode.cn id=2180 lang=cpp
 *
 * [2180] 统计各位数字之和为偶数的整数个数
 */

// @lc code=start
class Solution {
public:
    int countEven(int num) {
        int ret=0;
        for(int x=num;x>0;--x){
            if(!((x%10+(x/10)%10+(x/100)%10+(x/1000)%10)&1))++ret;
        }
        return ret;
    }
};
// @lc code=end

