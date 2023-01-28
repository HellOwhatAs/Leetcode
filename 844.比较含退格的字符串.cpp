/*
 * @lc app=leetcode.cn id=844 lang=cpp
 *
 * [844] 比较含退格的字符串
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    static void reduce(string & s) {
        int backspace = 0;
        while(!s.empty() && s.back() == '#'){
            s.pop_back();
            ++backspace;
            while(backspace){
                if(s.empty()) return;
                if(s.back() == '#'){
                    s.pop_back();
                    ++backspace;
                }
                else{
                    s.pop_back();
                    --backspace;
                }
            }
        }
    }
    bool backspaceCompare(string s, string t) {
        while(true){
            reduce(s);
            reduce(t);
            if(s.empty() && t.empty())return true;
            if(s.empty() || t.empty() || s.back() != t.back())return false;
            s.pop_back();
            t.pop_back();
        }
    }
};
// @lc code=end

