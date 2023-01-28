/*
 * @lc app=leetcode.cn id=231 lang=cpp
 *
 * [231] 2 的幂
 */

// @lc code=start
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return  n>0 && !(n&(n-1));
    }
};
// @lc code=end

0000000000000000000000000000010
0000000000000000000000000000001