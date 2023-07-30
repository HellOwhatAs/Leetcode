/*
 * @lc app=leetcode.cn id=66 lang=cpp
 *
 * [66] 加一
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    void func(vector<int>& digits, int start) {
        if(start == -1) {
            digits.insert(digits.begin(), 1);
            return;
        }
        ++digits[start];
        if(digits[start] / 10){
            digits[start] %= 10;
            func(digits, start - 1);
        }
    }
    vector<int> plusOne(vector<int>& digits) {
        func(digits, digits.size() - 1);
        return digits;
    }
};
// @lc code=end

