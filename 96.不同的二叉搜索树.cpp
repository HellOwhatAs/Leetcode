/*
 * @lc app=leetcode.cn id=96 lang=cpp
 *
 * [96] 不同的二叉搜索树
 */

// @lc code=start
#include<iostream>
using namespace std;
class Solution {
public:
    int arr[20];
    int func(int r){
        if(arr[r])return arr[r];
        int ret=0;
        for(int i=0;i<r;++i)ret+=func(i)*func(r-i-1);
        arr[r]=ret;
        return ret;
    }
    int numTrees(int n) {
        arr[0]=arr[1]=1;
        for(int i=2;i<n;++i)arr[i]=0;
        return func(n);
    }
};
// @lc code=end

