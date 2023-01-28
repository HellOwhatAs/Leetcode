/*
 * @lc app=leetcode.cn id=2351 lang=cpp
 *
 * [2351] 第一个出现两次的字母
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    char repeatedCharacter(string s) {
        bool d[256]={0};
        for(auto c:s){
            if(d[c])return c;
            d[c]=1;
        }
        return 0;
    }
};
// @lc code=end

