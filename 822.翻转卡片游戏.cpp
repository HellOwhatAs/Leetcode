/*
 * @lc app=leetcode.cn id=822 lang=cpp
 *
 * [822] 翻转卡片游戏
 */

// @lc code=start
#include<vector>
#include<unordered_set>
#include<climits>
#include<iostream>
using namespace std;
class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        unordered_set<int> same;
        int ret = INT_MAX;
        for(int i=0; i<fronts.size(); ++i){
            if(fronts[i] == backs[i]) same.insert(fronts[i]);
        }
        for(auto i: fronts){
            if(same.count(i)) continue;
            ret = min(ret, i);
        }
        for(auto i: backs){
            if(same.count(i)) continue;
            ret = min(ret, i);
        }
        return (ret == INT_MAX)? 0: ret; 
    }
};
// @lc code=end

