/*
 * @lc app=leetcode.cn id=1790 lang=cpp
 *
 * [1790] 仅执行一次字符串交换能否使两个字符串相等
 */

// @lc code=start
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> errs;
        for(int i=0;i<s1.size();++i){
            if(s1[i]!=s2[i]){
                if(errs.size()==2)return 0;
                errs.push_back(i);
            }
        }
        if(errs.size()==0)return 1;
        if(errs.size()==1)return 0;
        return s2[errs[1]]==s1[errs[0]] && s1[errs[1]]==s2[errs[0]];
    }
};
// @lc code=end

