/*
 * @lc app=leetcode.cn id=2315 lang=cpp
 *
 * [2315] 统计星号
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int countAsterisks(string s) {
        bool in = false;
        int ret = 0;
        for(char c: s){
            if(c == '|') in = !in;
            if(!in && c == '*') ++ ret;
        }
        return ret;
    }
};
// @lc code=end

