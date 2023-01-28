/*
 * @lc app=leetcode.cn id=13 lang=cpp
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
#include<map>
#include<string>
using namespace std;
class Solution {
public:
    map<char,int> d={
        {'I',1},
        {'V',5},
        {'X',10},
        {'L',50},
        {'C',100},
        {'D',500},
        {'M',1000}
    };
    int romanToInt(string s) {
        int _start=0,l=s.size(),ret=0,tmp;
        while(_start<l){
            tmp=d[s[_start]];
            ++_start;
            if(_start<l&&d[s[_start]]>tmp){
                tmp=d[s[_start]]-tmp;
                ++_start;
            }
            ret+=tmp;
        }
        return ret;
    }
};
// @lc code=end

