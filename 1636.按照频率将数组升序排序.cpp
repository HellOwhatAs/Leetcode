/*
 * @lc app=leetcode.cn id=1636 lang=cpp
 *
 * [1636] 按照频率将数组升序排序
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<algorithm>
using namespace std;
class Solution {
public:
    struct mycmp{
        unordered_map<int,int>* dd;
        mycmp(unordered_map<int,int>*_dd):dd(_dd){}
        bool operator()(int a,int b){
            if((*dd)[a]==(*dd)[b])return a>b;
            return (*dd)[a]<(*dd)[b];
        }
    };
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int,int> dict;
        for(auto&i:nums)++dict[i];
        sort(nums.begin(),nums.end(),mycmp(&dict));
        return nums;
    }
};
// @lc code=end

