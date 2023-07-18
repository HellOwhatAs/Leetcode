/*
 * @lc app=leetcode.cn id=1851 lang=cpp
 *
 * [1851] 包含每个查询的最小区间
 */

// @lc code=start
#include<vector>
#include<queue>
#include<algorithm>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        sort(intervals.begin(), intervals.end());
        vector<int> idxs(queries.size()), ret(queries.size(), -1);
        for(int i=0; i<idxs.size(); ++i) idxs[i] = i;
        sort(idxs.begin(), idxs.end(), [&](int a, int b){return queries[a] < queries[b];});
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        int idx = 0;
        for(auto i: idxs){
            while(idx < intervals.size() && intervals[idx][0] <= queries[i]){
                pq.push({intervals[idx][1] - intervals[idx][0] + 1, intervals[idx][1]});
                ++idx;
            }
            while(!pq.empty() && pq.top().second < queries[i]){
                pq.pop();
            }
            if(!pq.empty()) ret[i] = pq.top().first;
        }
        return ret;
    }
};
// @lc code=end

