/*
 * @lc app=leetcode.cn id=1703 lang=cpp
 *
 * [1703] 得到连续 K 个 1 的最少相邻交换次数
 */

// @lc code=start
#include<vector>
#include<queue>
#include<iostream>
#include<climits>
using namespace std;
class Solution {
public:
    int minMoves(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> pos;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                pos.push_back(i);
            }
        }
        int index = pos.size();
        int ans = 0, count = 0, mid = k / 2;
        for (int i = 1; i < k; i++) {
            count += (pos[i] - pos[i - 1] - 1) * min(i, k - i);
        }
        ans = count;
        for (int i = k; i < index; i++) {
            count -= pos[i - k + mid] - pos[i - k];
            count += pos[i] - pos[i - mid];
            ans = min(ans, count);
        }
        return ans;
    }
};
// @lc code=end

