/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] x 的平方根 
 */

// @lc code=start
class Solution {
public:
    int X;
    int func(int l,int r){
        if(l==r)return l;
        long mid=(long(l)+r)/2;
        return mid*mid>=X?func(l,mid):func(mid+1,r);
    }
    int mySqrt(int x) {
        X=x;
        auto ret=func(0,46340);
        if(ret*ret<=x)return ret;
        return ret-1;
    }
};
// @lc code=end

