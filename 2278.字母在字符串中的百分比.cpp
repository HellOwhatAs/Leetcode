/*
 * @lc app=leetcode.cn id=2278 lang=cpp
 *
 * [2278] 字母在字符串中的百分比
 */

// @lc code=start
#include<algorithm>
#include<string>
using namespace std;
class Solution {
public:
    int percentageLetter(string s, char letter) {
        return (100*count(s.begin(),s.end(),letter))/s.size();
    }
};
// @lc code=end

