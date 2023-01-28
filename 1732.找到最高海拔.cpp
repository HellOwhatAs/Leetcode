/*
 * @lc app=leetcode.cn id=1732 lang=cpp
 *
 * [1732] 找到最高海拔
 */

// @lc code=start
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int height=0,max_height=0;
        for(int i:gain){
            height+=i;
            max_height=max(max_height,height);
        }
        return max_height;
    }
};
// @lc code=end

