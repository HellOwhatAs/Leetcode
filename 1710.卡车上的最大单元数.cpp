/*
 * @lc app=leetcode.cn id=1710 lang=cpp
 *
 * [1710] 卡车上的最大单元数
 */

// @lc code=start
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        int ret=0;
        sort(boxTypes.begin(),boxTypes.end(),[](const vector<int>&a,const vector<int>&b){
            return a[1]<b[1];
        });
        while(!boxTypes.empty() && truckSize){
            ret+=boxTypes.back()[1];
            --truckSize;
            if(boxTypes.back()[0]==1)boxTypes.pop_back();
            else --boxTypes.back()[0];
        }
        return ret;
    }
};
// @lc code=end

