/*
 * @lc app=leetcode.cn id=2731 lang=cpp
 *
 * [2731] 移动机器人
 */

// @lc code=start
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
class Solution {
public:
    int sumDistance(vector<int>& nums, string s, int d) {
        int n = nums.size();
        for(int i=0; i<n; ++i){
            nums[i] += (s[i]=='L'? -1: 1) * d;
        }
        sort(nums.begin(), nums.end());
        long long int ret = 0;
        for(int i=1; i<n; ++i){
            ret += ((long long)nums[i] - nums[i-1])%1000000007 * i%1000000007 * (n - i);
            ret %= 1000000007;
        }
        return ret;
    }
};
// @lc code=end

