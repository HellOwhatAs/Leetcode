/*
 * @lc app=leetcode.cn id=834 lang=cpp
 *
 * [834] 树中距离之和
 */

// @lc code=start
#include<vector>
#include<unordered_set>
#include<optional>
#include<tuple>
using namespace std;
class Solution {
public:
    vector<unordered_set<int>> tree;
    vector<int> dp, sz, ret;
    
    void adjlist2tree(int start, optional<int> father = nullopt){
        if(father.has_value()) tree[start].erase(father.value());
        for(auto t: tree[start]) adjlist2tree(t, start);
    }

    void dfs0(int start){
        for(auto t: tree[start]){
            dfs0(t);
            sz[start] += sz[t];
            dp[start] += dp[t] + sz[t];
        }
    }
    // assuming `dp` and `sz` are initialized with `root` being root
    void swap_root(int child, int root){
        auto __backup__ = make_tuple(sz[root], sz[child], dp[root], dp[child]);
        dp[root] -= dp[child] + sz[child];
        sz[root] -= sz[child];
        sz[child] = get<0>(__backup__);
        dp[child] += dp[root] + sz[root];

        ret[child] = dp[child];
        for(auto t: tree[child]){
            swap_root(t, child);
        }

        tie(sz[root], sz[child], dp[root], dp[child]) = __backup__;
    }

    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        tree.resize(n, {});
        dp.resize(n, 0);
        sz.resize(n, 1);
        ret.resize(n);
        for(auto& edge: edges){
            tree[edge[0]].insert(edge[1]);
            tree[edge[1]].insert(edge[0]);
        }
        adjlist2tree(0);
        dfs0(0);
        ret[0] = dp[0];
        for(auto t: tree[0]){
            swap_root(t, 0);
        }
        return ret;
    }
};
// @lc code=end

