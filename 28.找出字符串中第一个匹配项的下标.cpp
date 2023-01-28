/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 找出字符串中第一个匹配项的下标
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    bool streq(const string&ha,int _start,const string&ne){
        for(int i=0;i<ne.size();++i){
            if(ne[i]!=ha[_start+i])return 0;
        }
        return 1;
    }
    int strStr(string haystack, string needle) {
        if(haystack.size()<needle.size())return -1;
        for(int i=0;i<=haystack.size()-needle.size();++i){
            if(streq(haystack,i,needle))return i;
        }
        return -1;
    }
};
// @lc code=end

