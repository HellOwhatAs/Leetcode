/*
 * @lc app=leetcode.cn id=1494 lang=cpp
 *
 * [1494] 并行课程 II
 */

// @lc code=start
#include<vector>
#include<climits>
#include<iostream>
#include<unordered_map>
#include<bitset>
using namespace std;
class Solution {
public:
    vector<vector<int>> adjlist;
    unordered_map<int, int> cache;
    int K;
    int hammingWeight(uint32_t n) {
        n = n - ((n >> 1) & 0x55555555);
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
        n = (n + (n >> 4)) & 0x0f0f0f0f;
        n = n + (n >> 8);
        n = n + (n >> 16);
        return n & 0x3f;
    }

    vector<vector<int>> combinations(const vector<int>& arr, int k) {
        vector<vector<int>> ret;
        for (int i = 0; i < (1 << arr.size()); ++i) {
            if (hammingWeight(i) != k) continue;
            ret.push_back({});
            int tmp = i, idx = 0;
            while (tmp) {
                if (tmp & 1) ret.back().push_back(arr[idx]);
                ++idx;
                tmp >>= 1;
            }
        }
        return ret;
    }

    int dfs(vector<int>& in_degrees, int vis) {
        if (cache.count(vis)) return cache[vis];
        return cache[vis] = __dfs(in_degrees, vis);
    }

    int __dfs(vector<int>& in_degrees, int vis) {
        if (vis == 0) return 0;
        vector<int> starts;
        for (int i = 0; i < in_degrees.size(); ++i) {
            if (in_degrees[i] == 0 && (vis & (1 << i))) starts.push_back(i);
        }
        int ret = INT_MAX;
        for (auto& candis : combinations(starts, min((int)starts.size(), K))) {
            for (auto cur : candis) {
                vis &= ~(1 << cur);
                for (auto neibour : adjlist[cur]) {
                    --in_degrees[neibour];
                }
            }
            ret = min(ret, dfs(in_degrees, vis));
            for (auto cur : candis) {
                vis |= (1 << cur);
                for (auto neibour : adjlist[cur]) {
                    ++in_degrees[neibour];
                }
            }
        }
        return ret + 1;
    }
    int minNumberOfSemesters(int n, const vector<vector<int>>& relations, int k) {
        adjlist.resize(n, {});
        cache.clear();
        K = k;
        vector<int> in_degrees(n, 0);
        for (auto& link : relations) {
            adjlist[link[0] - 1].push_back(link[1] - 1);
            ++in_degrees[link[1] - 1];
        }
        return dfs(in_degrees, (1 << n) - 1);
    }
};
// @lc code=end

