/*
 * @lc app=leetcode.cn id=791 lang=cpp
 *
 * [791] 自定义字符串排序
 */

// @lc code=start
#include<string>
#include<algorithm>
using namespace std;
class Solution {
public:
    string customSortString(string order, string s) {
        int d[256]={0};
        for(int i=0;i<order.size();++i)d[order[i]]=i;
        sort(s.begin(),s.end(),[&](char a,char b){return d[a]<d[b];});
        return s;
    }
};
// @lc code=end

