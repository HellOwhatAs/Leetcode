/*
 * @lc app=leetcode.cn id=1785 lang=cpp
 *
 * [1785] 构成特定和需要添加的最少元素
 */

// @lc code=start
#include<vector>
#include<numeric>
using namespace std;
class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        long long int ret=0, now=0, gap=goal;
        for(auto i:nums)gap-=i;
        if(gap<0)gap=-gap;
        return (gap+limit-1)/limit;
    }
};
// @lc code=end

