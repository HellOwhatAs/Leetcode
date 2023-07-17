/*
 * @lc app=leetcode.cn id=264 lang=cpp
 *
 * [264] 丑数 II
 */

// @lc code=start
#include<vector>
#include<tuple>
using namespace std;
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n);
        dp[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0;
        for(int i=1; i<n; ++i){
            auto[v2, v3, v5] = make_tuple(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5);
            auto val = dp[i] = min(v2, min(v3, v5));
            if(val == v2)++p2;
            if(val == v3)++p3;
            if(val == v5)++p5;
        }
        return dp.back();
    }
};
// @lc code=end

