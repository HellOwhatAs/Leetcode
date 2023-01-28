/*
 * @lc app=leetcode.cn id=1750 lang=cpp
 *
 * [1750] 删除字符串两端相同字符后的最短长度
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int minimumLength(string s) {
        int a=0, b=s.size()-1;
        char tmp;
        while(a<b){
            if(s[a]==s[b]){
                tmp=s[a];
                while(a<=b && s[a]==tmp)++a;
                while(a<=b && s[b]==tmp)--b;
            }
            else break;
        }
        return b-a+1;
    }
};
// @lc code=end
// "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"\n
// "cabaabac"\n