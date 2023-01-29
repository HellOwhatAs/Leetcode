/*
 * @lc app=leetcode.cn id=2148 lang=cpp
 *
 * [2148] 元素计数
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int countElements(vector<int>& nums) {
        int nmax = INT_MIN, nmin = INT_MAX, ret = 0;
        for(auto i: nums){
            nmax = max(nmax, i);
            nmin = min(nmin, i);
        }
        for(auto i:nums){
            ret += nmin < i && i < nmax;
        }
        return ret;
    }
};
// @lc code=end

