/*
 * @lc app=leetcode.cn id=1781 lang=cpp
 *
 * [1781] 所有子字符串美丽值之和
 */

// @lc code=start
#include<string>
#include<unordered_map>
#include<iostream>
#include<climits>
#include <algorithm>
using namespace std;
class Solution {
public:
    int beautySum(string s) {
        int res = 0, mx;
        unordered_map<char,int> cnt;
        for(int i=0;i<s.size();++i){
            cnt.clear();
            mx = 0;
            for(int j=i;j<s.size();++j){
                ++cnt[s[j]];
                mx = max(mx, cnt[s[j]]);
                res += mx - min_element(cnt.begin(),cnt.end(),[](const pair<char,int>&a, const pair<char,int>&b){return a.second<b.second;})->second;
            }
        }
        return res;
    }
};
// @lc code=end

