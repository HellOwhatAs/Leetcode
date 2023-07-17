/*
 * @lc app=leetcode.cn id=1685 lang=cpp
 *
 * [1685] 有序数组中差绝对值之和
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        vector<int> ret(nums.size()), ret2(nums.size());
        for(int i=1; i<ret.size(); ++i){
            ret[i] = ret[i-1] + i * (nums[i] - nums[i-1]);
        }
        reverse(nums.begin(), nums.end());
        for(int i=1; i<ret2.size(); ++i){
            ret2[i] = ret2[i-1] + i * (nums[i-1] - nums[i]);
            ret[ret.size() - 1 - i] += ret2[i];
        }
        return ret;
    }
};
// @lc code=end

