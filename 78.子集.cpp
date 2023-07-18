/*
 * @lc app=leetcode.cn id=78 lang=cpp
 *
 * [78] 子集
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ret(1<<nums.size());
        for(int i=0; i<ret.size(); ++i){
            int tmp = i, idx = 0;
            while(tmp){
                if(tmp & 1) ret[i].push_back(nums[idx]);
                tmp >>= 1;
                ++idx;
            }
        }
        return ret;
    }
};
// @lc code=end

