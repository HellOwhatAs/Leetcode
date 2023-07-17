/*
 * @lc app=leetcode.cn id=264 lang=cpp
 *
 * [264] 丑数 II
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n);
        dp[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0;
        for(int i=1; i<n; ++i){
            vector<int> candidates = {dp[p2] * 2, dp[p3] * 3, dp[p5] * 5};
            auto val = dp[i] = min(candidates[0], min(candidates[1], candidates[2]));
            if(val == candidates[0])++p2;
            if(val == candidates[1])++p3;
            if(val == candidates[2])++p5;
        }
        return dp.back();
    }
};
// @lc code=end

