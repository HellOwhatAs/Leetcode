/*
 * @lc app=leetcode.cn id=2027 lang=cpp
 *
 * [2027] 转换字符串的最少操作次数
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int minimumMoves(string s) {
        int i=0, ret=0;
        while(i<s.size()){
            if(s[i]=='X'){
                i+=3;
                ++ret;
            }
            else ++i;
        }
        return ret;
    }
};
// @lc code=end

