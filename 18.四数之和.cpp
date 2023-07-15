/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */

// @lc code=start
#include<vector>
#include<unordered_set>
#include<tuple>
#include<algorithm>
#include<climits>
using namespace std;
class Solution {
public:
    struct tuple_hash {
    	int operator() (const std::tuple<int, int, int, int>& x) const {
    		unsigned int a, b, c, d;
            tie(a, b, c, d) = x;
            return (((((a * 37) ^ b) * 37) ^ c) * 37) ^ d;
    	}
    };
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if(nums.size() < 4) return {};
        unordered_set<tuple<int, int, int, int>, tuple_hash> ret;
        sort(nums.begin(), nums.end());
        for(int a=0; a<nums.size()-3; ++a){
            for(int b=a+1; b<nums.size()-2; ++b){
                int c = b + 1, d = nums.size() - 1;
                long long tmp = (long long)target - nums[a] - nums[b], cd;
                while(c < d){
                    cd = (long long)nums[c] + nums[d];
                    if(cd == tmp) ret.insert({nums[a], nums[b], nums[c], nums[d]});
                    if(cd < tmp) ++c;
                    else --d;
                }
            }
        }
        vector<vector<int>> rret;
        for(auto&[na, nb, nc, nd]: ret){
            rret.push_back({na, nb, nc, nd});
        }
        return rret;
    }
};
// @lc code=end

