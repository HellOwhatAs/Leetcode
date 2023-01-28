/*
 * @lc app=leetcode.cn id=698 lang=cpp
 *
 * [698] 划分为k个相等的子集
 */

// @lc code=start
#include<vector>
#include<algorithm>
#include<numeric>
using namespace std;
class Solution {
public:
    vector<int>* v;
    int *arr,_k;
    bool valid(int ind, int limit){
        if(ind==v->size())return true;
        for(int i=0;i<_k;++i){
            if((*v)[ind]+arr[i]<=limit){
                arr[i]+=(*v)[ind];
                if(valid(ind+1,limit))return true;
                arr[i]-=(*v)[ind];
            }
            if(arr[i]==0||arr[i]+(*v)[ind]==limit)return false;
        }
        return false;
    }
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end(),greater<int>());
        v=&nums;
        _k=k;
        arr=new int[k];
        for(int i=0;i<k;++i)arr[i]=0;
        return valid(0,accumulate(nums.begin(),nums.end(),0)/k);
    }
};
// @lc code=end

