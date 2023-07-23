/*
 * @lc app=leetcode.cn id=407 lang=cpp
 *
 * [407] 接雨水 II
 */

// @lc code=start
#include<vector>
#include<queue>
#include<unordered_set>
using namespace std;
class Solution {
public:
    struct pair_hash {
        int operator()(const pair<int, int>& a) const {
            return (a.first + 37) ^ a.second;
        };
    };
    int trapRainWater(const vector<vector<int>>& heightMap) {
        int m = heightMap.size(), n = heightMap.front().size();
        vector<vector<int>> water = heightMap;
        auto cmp = [&](const pair<int, int>& a, const pair<int, int>& b) {
            return water[a.first][a.second] > water[b.first][b.second];
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        unordered_set<pair<int, int>, pair_hash> vis;
        for (int i = 0; i < m; ++i) {
            pq.push({ i, 0 });
            vis.insert({ i, 0 });
            pq.push({ i, n - 1 });
            vis.insert({ i, n - 1 });
        }
        for (int j = 1; j < n - 1; ++j) {
            pq.push({ 0, j });
            vis.insert({ 0, j });
            pq.push({ m - 1, j });
            vis.insert({ m - 1, j });
        }
        while (vis.size() < m * n) {
            auto [i, j] = pq.top(); pq.pop();
            for (auto [i1, j1] : vector<pair<int, int>>({ {i - 1, j}, {i, j - 1}, {i + 1, j}, {i, j + 1} })) {
                if (i1 < 0 || i1 >= m || j1 < 0 || j1 >= n || vis.count({ i1, j1 })) continue;
                water[i1][j1] = max(water[i1][j1], water[i][j]);
                pq.push({ i1, j1 });
                vis.insert({ i1, j1 });
            }
        }
        int ret = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ret += water[i][j] - heightMap[i][j];
            }
        }
        return ret;
    }
};
// @lc code=end

