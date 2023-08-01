/*
 * @lc app=leetcode.cn id=2681 lang=cpp
 *
 * [2681] 英雄的力量
 */

// @lc code=start
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    int sumOfPower(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long int dp, pre_sum = 0, res = 0, mod = 1000000007;
        for(long long int num: nums){
            dp = (pre_sum + num) % mod;
            pre_sum = (pre_sum + dp) % mod;
            res = (res + (num * num) % mod * dp) % mod;
        }
        return res;
    }
};
// @lc code=end

