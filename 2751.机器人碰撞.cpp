/*
 * @lc app=leetcode.cn id=2751 lang=cpp
 *
 * [2751] 机器人碰撞
 */

// @lc code=start
#include<vector>
#include<string>
#include<algorithm>
#include<numeric>
#include<queue>
#include<functional>
using namespace std;

class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> idxer(n);
        iota(idxer.begin(), idxer.end(), 0);
        sort(idxer.begin(), idxer.end(), [&](int x, int y){return positions[x] < positions[y];});
        vector<pair<int, int>> heap_input(n - 1);
        for(int i=1; i<n; ++i) heap_input.push_back({i-1, i});
        priority_queue<pair<int, int>, vector<pair<int, int>>, 
            function<bool(const pair<int, int>&, const pair<int, int>&)>> collisions(
            [&](const pair<int, int>& a, const pair<int, int>& b) {
                return positions[a.second] - positions[a.first] > positions[b.second] - positions[b.first];
            }, heap_input
        );
        while (!collisions.empty()) {
            auto [ii, jj] = collisions.top(); collisions.pop();
            int i = idxer[ii], j = idxer[jj];
            if(!(directions[i] == 'R' && directions[j] == 'L')) continue;
            if(healths[i] == healths[j]) {
                healths[i] = healths[j] = 0;
                while (ii >= 0 && healths[idxer[ii]] == 0) --ii;
                if(ii < 0) continue;
                while (jj < n && healths[idxer[jj]] == 0) ++jj;
                if(jj >= n) continue;
            }
            else if (healths[i] > healths[j]) {
                --healths[i];
                healths[j] = 0;
                while (jj < n && healths[idxer[jj]] == 0) ++jj;
                if(jj >= n) continue;
            }
            else {
                healths[i] = 0;
                --healths[j];
                while (ii >= 0 && healths[idxer[ii]] == 0) --ii;
                if(ii < 0) continue;
            }
            collisions.push({ii, jj});
        }

        idxer.clear();
        for(auto i: healths){
            if(i > 0) idxer.push_back(i);
        }
        return idxer;
    }
};
// @lc code=end

