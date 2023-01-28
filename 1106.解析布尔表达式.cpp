/*
 * @lc app=leetcode.cn id=1106 lang=cpp
 *
 * [1106] 解析布尔表达式
 */

// @lc code=start
#include<string>
#include<stack>
using namespace std;
class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> s;
        int tcount,fcount;
        for(auto i:expression){
            switch(i){
            case 't':
                s.push('t');
                break;
            case 'f':
                s.push('f');
                break;
            case '!':
                s.push('!');
                break;
            case '&':
                s.push('&');
                break;
            case '|':
                s.push('|');
                break;
            case ')':
                tcount=fcount=0;
                while(s.top()=='t'||s.top()=='f'){
                    if(s.top()=='t')tcount++;
                    else fcount++;
                    s.pop();
                }
                switch(s.top()){
                case '&':
                    s.pop();
                    if(fcount)s.push('f');
                    else s.push('t');
                    break;
                case '|':
                    s.pop();
                    if(tcount)s.push('t');
                    else s.push('f');
                    break;
                default:
                    s.pop();
                    if(tcount)s.push('f');
                    else s.push('t');
                    break;
                }
                break;
            default:
                break;
            }
        }
        return s.top()=='t';
    }
};
// @lc code=end

