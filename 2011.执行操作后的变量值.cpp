/*
 * @lc app=leetcode.cn id=2011 lang=cpp
 *
 * [2011] 执行操作后的变量值
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ret=0;
        for(auto&i:operations)if(i[1]=='+')++ret;
        return 2*ret-operations.size();
    }
};
// @lc code=end

