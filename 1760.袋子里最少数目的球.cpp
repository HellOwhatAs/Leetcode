/*
 * @lc app=leetcode.cn id=1760 lang=cpp
 *
 * [1760] 袋子里最少数目的球
 */

// @lc code=start
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;
class Solution {
public:
    template<class T>
    int bisect(int left, int right, const T&val, const function<T(int)>&f){
        int ans = -1, mid;
        while(left<=right){
            mid=(left+right)/2;
            if(f(mid)<=val){ans=mid;right=mid-1;}
            else left=mid+1;
        }
        return ans;
    }
    int minimumSize(vector<int>& nums, int maxOperations) {
        return bisect<long long>(1, *max_element(nums.begin(), nums.end()), maxOperations, 
        [&nums](int i){
            long long int ret=0;
            for (int x: nums)ret+=(x-1)/i;
            return ret;
        });
    }
};
// @lc code=end

