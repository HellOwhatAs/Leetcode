/*
 * @lc app=leetcode.cn id=869 lang=cpp
 *
 * [869] 重新排序得到 2 的幂
 */

// @lc code=start
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    bool eq(const string& a, const string& b) {
        vector<int> arr(10, 0);
        for(auto c: a) ++arr[c - '0'];
        for(auto c: b) --arr[c - '0'];
        for(auto i: arr) if(i != 0) return false;
        return true;
    }
    bool reorderedPowerOf2(int n) {
        int val = 1;
        while(to_string(val).size() < to_string(n).size()) val <<= 1;
        while(to_string(val).size() == to_string(n).size()) {
            if(eq(to_string(val), to_string(n))) return true;
            val <<= 1;
        }
        return false;
    }
};
// @lc code=end

