/*
 * @lc app=leetcode.cn id=813 lang=cpp
 *
 * [813] 最大平均值和的分组
 */

// @lc code=start
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int k) {
        double dp[102][102]={0};
        int n=nums.size(),prefix[102]={0};
        for(int i=1;i<n+1;++i){
            prefix[i]=prefix[i-1]+nums[i-1];
            dp[i][1]=double(prefix[i])/i;
        }
        for(int j=2;j<k+1;++j){
            for(int i=j;i<n+1;++i){
                for(int x=j-1;x<i;++x){
                    dp[i][j]=max(dp[i][j],dp[x][j-1]+double(prefix[i]-prefix[x])/(i-x));
                }
            }
        }
        return dp[n][k];
    }
};
// @lc code=end

