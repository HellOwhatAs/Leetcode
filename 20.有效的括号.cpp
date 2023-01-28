/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */

// @lc code=start
#include<stack>
#include<string>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<char> t;
        for(auto i:s){
            if(i=='('||i=='{'||i=='[')t.push(i);
            else{
                if(t.empty())return 0;
                if(i==')'){
                    
                    if(t.top()=='(')t.pop();
                    else return 0;
                }
                if(i=='}'){
                    if(t.top()=='{')t.pop();
                    else return 0;
                }
                if(i==']'){
                    if(t.top()=='[')t.pop();
                    else return 0;
                }
            }
        }
        return t.empty();
    }
};
// @lc code=end

