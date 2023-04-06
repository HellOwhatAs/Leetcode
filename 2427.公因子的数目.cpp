/*
 * @lc app=leetcode.cn id=2427 lang=cpp
 *
 * [2427] 公因子的数目
 */

// @lc code=start
class Solution {
public:
    int commonFactors(int a, int b) {
        int ret = 1;
        for(int i = 2; i <= min(a, b); ++i) {
            ret += (a % i == 0 && b % i == 0);
        }
        return ret;
    }
};
// @lc code=end

