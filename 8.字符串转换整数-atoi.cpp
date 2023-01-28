/*
 * @lc app=leetcode.cn id=8 lang=cpp
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
#include<string>
#include<climits>
using namespace std;
class Solution {
public:
    int myAtoi(string s) {
        string ret;
        auto i=s.begin();
        while(*i==' ')++i;
        if(*i=='+')++i;
        else if(*i=='-'){
            ret.push_back('-');
            ++i;
        }
        while((*i)=='0')++i;
        while((*i)<='9'&&(*i)>='0'){
            ret.push_back(*i);
            ++i;
        }
        if(ret.size()>10+(ret[0]=='-')){
            if(ret[0]=='-')return INT_MIN;
            return INT_MAX;
        }
        return min(max(atol(ret.c_str()),long(INT_MIN)),long(INT_MAX));
    }
};
// @lc code=end

