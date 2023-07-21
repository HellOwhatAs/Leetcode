/*
 * @lc app=leetcode.cn id=1499 lang=cpp
 *
 * [1499] 满足不等式的最大值
 */

// @lc code=start
#include<vector>
#include<queue>
#include<climits>
using namespace std;
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        deque<int> q;
        int ret = INT_MIN; 
        for(int j=0; j<points.size(); ++j){
            int xj = points[j][0], yj = points[j][1];
            while(!q.empty() && xj - points[q.front()][0] > k) q.pop_front();
            if(!q.empty()) ret = max(ret, xj + yj + points[q.front()][1] - points[q.front()][0]);
            while(!q.empty() && points[q.back()][1] - points[q.back()][0] < yj - xj) q.pop_back();
            q.push_back(j);
        }
        return ret;
    }
};
// @lc code=end

