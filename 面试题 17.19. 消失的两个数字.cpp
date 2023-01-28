#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> missingTwo(vector<int>& nums) {
        vector<int> ret;
        nums.push_back(0);
        nums.push_back(0);
        int n=nums.size();
        for(int i=0;i<n;++i){
            while(nums[i]!=i+1&&nums[i]!=0){
                swap(nums[i],nums[nums[i]-1]);
            }
        }
        for(int i=0;i<n;++i){
            if(!nums[i])ret.push_back(i+1);
        }
        return ret;
    }
};