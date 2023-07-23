/*
 * @lc app=leetcode.cn id=131 lang=cpp
 *
 * [131] 分割回文串
 */

// @lc code=start
#include<vector>
#include<optional>
#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    optional<vector<string>> func(int mask, const string& s){
        int idx = 1;
        vector<int> idxs = {0};
        vector<string> ret;
        while(mask){
            if(mask & 1) idxs.push_back(idx);
            mask >>= 1;
            ++idx;
        }
        idxs.push_back(s.size());
        for(int i=1; i<idxs.size(); ++i){
            string tmp = s.substr(idxs[i-1], idxs[i] - idxs[i-1]);
            ret.push_back(tmp);
            reverse(tmp.begin(), tmp.end());
            if(ret.back() != tmp) {
                return nullopt;
            }
        }
        return ret;
    }
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ret;
        for(int mask = 0; mask < (1<<(s.size()-1)); ++mask){
            auto tmp = func(mask, s);
            if(tmp.has_value()) {
                ret.emplace_back(tmp.value());
            }
        }
        return ret;
    }
};
// @lc code=end

