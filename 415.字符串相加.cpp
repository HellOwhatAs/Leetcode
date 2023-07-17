/*
 * @lc app=leetcode.cn id=415 lang=cpp
 *
 * [415] 字符串相加
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string ret;
    void func(const string& n1, const string& n2, int idx, int carry = 0) {
        if(n1.size() <= idx && n2.size() <= idx && carry == 0) return;
        int tmp = (idx < n1.size()? n1[idx] - '0': 0) + (idx < n2.size()? n2[idx] - '0': 0) + carry;
        ret.push_back(tmp % 10 + '0');
        func(n1, n2, idx + 1, tmp / 10);
    }
    string addStrings(string num1, string num2) {
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        ret.clear();
        func(num1, num2, 0);
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
// @lc code=end

