/*
 * @lc app=leetcode.cn id=1684 lang=cpp
 *
 * [1684] 统计一致字符串的数目
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int d[128]={0},ret=words.size();
        for(auto i:allowed)d[i]=1;
        for(auto&i:words){
            for(auto j:i){
                if(!d[j]){
                    --ret;
                    break;
                }
            }
        }
        return ret;
    }
};
// @lc code=end

