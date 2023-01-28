/*
 * @lc app=leetcode.cn id=792 lang=cpp
 *
 * [792] 匹配子序列的单词数
 */

// @lc code=start
#include<vector>
#include<string>
#include<unordered_map>
#include<algorithm>
#include<iostream>
using namespace std;
class Solution {
public:
    bool inthere(const vector<vector<int>>&ds,const string&x){
        int start=0;
        for(auto i:x){
            auto k=lower_bound(ds[i-'a'].begin(),ds[i-'a'].end(),start);
            if(k==ds[i-'a'].end())return false;
            start=*k+1;
        }
        return true;
    }
    int numMatchingSubseq(string s, vector<string>& words) {
        vector<vector<int>> ds(26);
        for(int i=0;i<s.size();++i){
            ds[s[i]-'a'].push_back(i);
        }
        int ret=0;
        for(auto&i:words){
            if(inthere(ds,i)){
                ++ret;
            }
        }
        return ret;
    }
};
// @lc code=end

