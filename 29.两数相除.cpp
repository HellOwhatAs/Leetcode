/*
 * @lc app=leetcode.cn id=29 lang=cpp
 *
 * [29] 两数相除
 */

// @lc code=start
#include<climits>
class Solution {
public:
    int divide(int dividend, int divisor) {
        if(!dividend)return 0;
        int ret=0,count=1;
        bool flag=0;
        if(dividend>0){dividend=-dividend;flag=!flag;}
        if(divisor>0){divisor=-divisor;flag=!flag;}
        while(divisor>(INT_MIN>>1)&&(divisor+divisor)>dividend){
            divisor+=divisor;
            count<<=1;
        }
        while(dividend){
            while(dividend>divisor){
                divisor>>=1;
                count>>=1;
            }
            if(!count)break;
            while(dividend<=divisor){
                dividend-=divisor;
                ret-=count;
            }
        }
        return (!flag)?(ret==INT_MIN?INT_MAX:-ret):ret;
    }
};
// @lc code=end

