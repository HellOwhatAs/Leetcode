/*
 * @lc app=leetcode.cn id=1723 lang=cpp
 *
 * [1723] 完成所有工作的最短时间
 */
// [6518448,8819833,7991995,7454298,2087579,380625,4031400,2905811,4901241,8480231,7750692,3544254]
// 4 
// @lc code=start
#include<vector>
#include <numeric>
#include<algorithm>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> *v;
    int _k,*arr;
    bool _valid(int ind, int limit){
        if(ind==v->size())return true;
        for(int i=0;i<_k;++i){
            if((*v)[ind]+arr[i]<=limit){
                arr[i]+=(*v)[ind];
                if(_valid(ind+1,limit))return true;
                arr[i]-=(*v)[ind];
            }
            if(arr[i]==0||arr[i]+(*v)[ind]==limit)return false;
        }
        return false;
    }
    bool valid(int ind, int limit){
        for(int i=0;i<_k;++i)arr[i]=0;
        return _valid(ind,limit);
    }
    int minimumTimeRequired(vector<int>& jobs, int k) {
        v=&jobs;_k=k;arr=new int[k];
        sort(jobs.begin(),jobs.end(),greater<int>());
        int ub=accumulate(jobs.begin(),jobs.end(),0),lb=ub/k;
        if(valid(0,lb))return lb;
        while(lb+1<ub){
            int mid=(ub+lb)/2;
            if(valid(0,mid))ub=mid;
            else lb=mid;
        }
        delete [] arr;
        return ub;
    }
};
// @lc code=end

