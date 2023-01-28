/*
 * @lc app=leetcode.cn id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */

// @lc code=start
class Solution {
public:
    double myPow(double x, int n) {
        if(n==0)return 1;
        if(!(n%2))return myPow(x*x,n/2);
        return myPow(x*x,n/2)*(n>0?x:1/x);
    }
};
// @lc code=end

