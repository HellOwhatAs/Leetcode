/*
 * @lc app=leetcode.cn id=1844 lang=cpp
 *
 * [1844] 将所有数字用字符替换
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    static char shift(char c, char x){
        return c + x - '0';
    }
    string replaceDigits(string s) {
        for(int i = 1; i < s.size(); i += 2){
            s[i] = shift(s[i-1], s[i]);
        }
        return s;
    }
};
// @lc code=end

