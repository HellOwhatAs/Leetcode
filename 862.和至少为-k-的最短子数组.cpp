/*
 * @lc app=leetcode.cn id=862 lang=cpp
 *
 * [862] 和至少为 K 的最短子数组
 */

// @lc code=start
#include<vector>
#include<deque>
using namespace std;
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        vector<long long int> a={0};
        for(auto i:nums)a.push_back(a.back()+i);
        deque<int> q;
        int ret=INT_MAX;
        for(int i=0;i<a.size();++i){
            while(!q.empty()&&a[i]-a[q.front()]>=k){
                ret=min(ret,i-q.front());
                q.pop_front();
            }
            while(!q.empty()&&a[q.back()]>=a[i]){
                q.pop_back();
            }
            q.push_back(i);
        }
        return ret==INT_MAX?-1:ret;
    }
};
// @lc code=end

