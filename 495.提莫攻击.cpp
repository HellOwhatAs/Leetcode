/*
 * @lc app=leetcode.cn id=495 lang=cpp
 *
 * [495] 提莫攻击
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int ret = 0, free = 0;
        for(auto t: timeSeries) {
            if(t < free) ret -= free - t;
            free = t + duration;
            ret += duration;
        }
        return ret;
    }
};
// @lc code=end

