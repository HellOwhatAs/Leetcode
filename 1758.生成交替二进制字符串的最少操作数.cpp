/*
 * @lc app=leetcode.cn id=1758 lang=cpp
 *
 * [1758] 生成交替二进制字符串的最少操作数
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int minOperations(string s) {
        int ret=0;
        for(int i=0;i<s.size();++i){
            if('0'+i%2!=s[i])++ret;
        }
        return min(size_t(ret),s.size()-ret);
    }
};
// @lc code=end

