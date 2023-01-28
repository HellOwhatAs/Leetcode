/*
 * @lc app=leetcode.cn id=704 lang=cpp
 *
 * [704] 二分查找
 */

// @lc code=start
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto i=lower_bound(nums.begin(),nums.end(),target);
        if(i==nums.end()||(*i)!=target)return -1;
        return i-nums.begin();
    }
};
// @lc code=end

