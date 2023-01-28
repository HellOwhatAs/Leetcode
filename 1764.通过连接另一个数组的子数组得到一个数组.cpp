/*
 * @lc app=leetcode.cn id=1764 lang=cpp
 *
 * [1764] 通过连接另一个数组的子数组得到一个数组
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    template<class T>
    int find(const vector<T>&x, const vector<T>&y, int start=0){
        int ret=start, i;
        while(ret<x.size()){
            for(i=0;i<y.size();++i){
                if(y[i]!=x[ret+i])break;
            }
            if(i==y.size())return ret;
            ++ret;
        }
        return -1;
    }
    bool canChoose(vector<vector<int>>& groups, vector<int>& nums) {
        int s=0, tmp;
        for(auto&group:groups){
            tmp = find(nums,group,s);
            if(tmp==-1)return false;
            s=tmp+group.size();
        }
        return true;
    }
};
// @lc code=end

