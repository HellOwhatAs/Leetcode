/*
 * @lc app=leetcode.cn id=2208 lang=cpp
 *
 * [2208] 将数组和减半的最少操作次数
 */

// @lc code=start
#include<vector>
#include<queue>
#include<numeric>
using namespace std;
class Solution {
public:
    int halveArray(const vector<int>& nums) {
        priority_queue<double> pq(nums.begin(), nums.end());
        int ret = 0;
        double target = accumulate(nums.begin(), nums.end(), 0.) / 2;
        while(target > 0){
            auto tmp = pq.top() / 2; pq.pop();
            pq.push(tmp);
            target -= tmp;
            ++ret;
        }
        return ret;
    }
};
// @lc code=end

