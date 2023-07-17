/*
 * @lc app=leetcode.cn id=2446 lang=cpp
 *
 * [2446] 判断两个事件是否存在冲突
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    int str2int(const string& time) {
        return ((time[0] - '0') * 10 + time[1] - '0') * 60 + (time[3] - '0') * 10 + time[4] - '0';
    }
    bool haveConflict(vector<string>& event1, vector<string>& event2) {
        return !(str2int(event1[1]) < str2int(event2[0])  || str2int(event2[1]) < str2int(event1[0]));
    }
};
// @lc code=end

