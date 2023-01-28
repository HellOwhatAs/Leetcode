/*
 * @lc app=leetcode.cn id=754 lang=cpp
 *
 * [754] 到达终点数字
 */

// @lc code=start
class Solution {
public:
    int reachNumber(int target) {
        int i=1,s=0;
        if(target<0)target=-target;
        while(target>s){
            s+=i;
            ++i;
        }
        while((s-target)%2){
            s+=i;
            ++i;
        }
        return i-1;
    }
};
// @lc code=end

