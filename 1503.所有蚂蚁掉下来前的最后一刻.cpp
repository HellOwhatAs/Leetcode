/*
 * @lc app=leetcode.cn id=1503 lang=cpp
 *
 * [1503] 所有蚂蚁掉下来前的最后一刻
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        return max((right.empty()? 0 : n - *min_element(right.begin(), right.end())), (left.empty()? 0 : *max_element(left.begin(), left.end())));
    }
};
// @lc code=end

