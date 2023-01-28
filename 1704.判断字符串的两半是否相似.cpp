/*
 * @lc app=leetcode.cn id=1704 lang=cpp
 *
 * [1704] 判断字符串的两半是否相似
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    bool halvesAreAlike(string s) {
        int c=0;
        for(int i=0;i<s.size()/2;++i){
            switch(s[i]){
            case 'a':++c;break;
            case 'e':++c;break;
            case 'i':++c;break;
            case 'o':++c;break;
            case 'u':++c;break;
            case 'A':++c;break;
            case 'E':++c;break;
            case 'I':++c;break;
            case 'O':++c;break;
            case 'U':++c;break;
            }
        }
        for(int i=s.size()/2;i<s.size();++i){
            switch(s[i]){
            case 'a':--c;break;
            case 'e':--c;break;
            case 'i':--c;break;
            case 'o':--c;break;
            case 'u':--c;break;
            case 'A':--c;break;
            case 'E':--c;break;
            case 'I':--c;break;
            case 'O':--c;break;
            case 'U':--c;break;
            }
        }
        return c==0;
    }
};
// @lc code=end

