/*
 * @lc app=leetcode.cn id=2050 lang=cpp
 *
 * [2050] 并行课程 III
 */

// @lc code=start
#include<vector>
#include<queue>
using namespace std;
class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> adjlist(n);
        vector<int> in_degrees(n, 0), earlist(n, 0);
        for(auto& link: relations) {
            adjlist[link[0]-1].push_back(link[1]-1);
            ++in_degrees[link[1]-1];
        }
        queue<int> q;
        for(int i=0; i<n; ++i){
            if(in_degrees[i] == 0){
                q.push(i);
                earlist[i] = time[i];
            }
        }
        while(!q.empty()){
            int cur = q.front(); q.pop();
            for(int neibour: adjlist[cur]) {
                --in_degrees[neibour];
                earlist[neibour] = max(earlist[neibour], earlist[cur] + time[neibour]);
                if(in_degrees[neibour] == 0){
                    q.push(neibour);
                }
            }
        }
        return *max_element(earlist.begin(), earlist.end());
    }
};
// @lc code=end

