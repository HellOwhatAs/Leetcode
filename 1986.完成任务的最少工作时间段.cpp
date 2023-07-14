/*
 * @lc app=leetcode.cn id=1986 lang=cpp
 *
 * [1986] 完成任务的最少工作时间段
 */

// @lc code=start
#include<vector>
#include<climits>
#include<tuple>
using namespace std;
class Solution {
public:
    int minSessions(const vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        auto* dp = new pair<int, int>[1<<n];
        dp[0] = {1, 0};
        for(int mask=1; mask<(1<<n); ++mask){
            dp[mask] = {INT_MAX, INT_MAX};
            for(int i=0; i<n; ++i){
                if(mask & (1<<i)){
                    int pre_num, pre_last;
                    tie(pre_num, pre_last) = dp[mask ^ (1<<i)];
                    if(pre_last + tasks[i] > sessionTime) ++pre_num, pre_last = tasks[i];
                    else pre_last += tasks[i];
                    dp[mask] = min(dp[mask], {pre_num, pre_last});
                }
            }
        }
        return dp[(1<<n)-1].first;
    }
};
// @lc code=end
#include<iostream>
int main(){
    cout << Solution().minSessions({1,2,3}, 3) << '\n'
         << Solution().minSessions({3,1,3,1,1}, 8) << '\n'
         << Solution().minSessions({1,2,3,4,5}, 15) << '\n';
    return 0;
}