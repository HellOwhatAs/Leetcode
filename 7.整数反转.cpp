/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 */

// @lc code=start
#include<climits>
class Solution {
public:
    int reverse(int x) {
        int ret=0;
        while(x){
            if(INT_MAX/10<ret||INT_MIN/10>ret)return 0;
            ret=ret*10+x%10;
            x/=10;
        }
        return ret;
    }
};
// @lc code=end

