/*
 * @lc app=leetcode.cn id=167 lang=cpp
 *
 * [167] 两数之和 II - 输入有序数组
 */
#include<iostream>
// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(const vector<int>& numbers, int target) {
        int i = 0, j = numbers.size() - 1, tmp;
        while (i < j) {
            tmp = numbers[i] + numbers[j];
            if (tmp == target) return {i + 1, j + 1};
            if (tmp > target) --j;
            else ++i;
        }
        throw pair<int, int>(i, j);
    }
};
// @lc code=end

int main() {
    auto res = Solution().twoSum({-1,0}, -1);
    for(auto elem = res.begin(); elem != res.end(); ++elem) cout << (*elem) << ' ';
    return 0;
}