/*
 * @lc app=leetcode.cn id=1691 lang=cpp
 *
 * [1691] 堆叠长方体的最大高度
 */

// @lc code=start
#include<vector>
#include<algorithm>
#include<iostream>
#include<numeric>
using namespace std;
class Solution {
public:
    int maxHeight(vector<vector<int>>& cuboids) {
        int n=cuboids.size();
        vector<int> dp(n,0);
        auto vle_all=[](const vector<int>& a, const vector<int>& b){
            return a[0]<=b[0] && a[1]<=b[1] && a[2]<=b[2];
        };
        auto vsumle=[](const vector<int>& a, const vector<int>& b){
            return accumulate(a.begin(),a.end(),0)<accumulate(b.begin(),b.end(),0);
        };
        for(auto&i:cuboids)sort(i.begin(),i.end());
        sort(cuboids.begin(),cuboids.end(),vsumle);
        for(int i=0;i<n;++i){
            for(int j=0;j<i;++j){
                if(vle_all(cuboids[j],cuboids[i])){
                    dp[i]=max(dp[i],dp[j]);
                }
            }
            dp[i]+=cuboids[i][2];
        }
        return *max_element(dp.begin(),dp.end());
    }
};
// @lc code=end

//[[88,45,69],[88,15,96],[49,78,68],[96,72,80],[80,86,13],[9,99,73],[94,42,39],[30,19,58],[10,32,21],[20,52,85]]