/*
 * @lc app=leetcode.cn id=2404 lang=cpp
 *
 * [2404] 出现最频繁的偶数元素
 */

// @lc code=start
#include<unordered_map>
using namespace std;
class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        unordered_map<int,int> dict;
        for(auto&i:nums){
            if(!(i%2)){
                ++dict[i];
            }
        }
        if(!dict.size())return -1;
        int _max=0,maxind=-1;
        for(auto&i:dict){
            if(i.second>_max||i.second==_max&&i.first<maxind){
                _max=i.second;
                maxind=i.first;
            }
        }
        return maxind;
    }
};
// @lc code=end

