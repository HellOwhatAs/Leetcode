/*
 * @lc app=leetcode.cn id=769 lang=cpp
 *
 * [769] 最多能完成排序的块
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int ret=0,maxhere=-1;
        for(int i=0;i<arr.size();++i){
            maxhere=max(maxhere,arr[i]);
            if(i>=maxhere)++ret;
        }
        return ret;
    }
};
// @lc code=end

