/*
 * @lc app=leetcode.cn id=2544 lang=cpp
 *
 * [2544] 交替数字和
 */

// @lc code=start
class Solution {
public:
    int alternateDigitSum(int n) {
        int ret = 0;
        bool flag = 0;
        while (n) {
            ret += (flag ? -1 : 1) * (n % 10);
            n /= 10;
            flag = !flag;
        }
        return (flag ? 1 : -1) * ret;
    }
};
// @lc code=end

