/*
 * @lc app=leetcode.cn id=703 lang=cpp
 *
 * [703] 数据流中的第 K 大元素
 */

// @lc code=start
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
class KthLargest {
public:
    priority_queue<int,vector<int>,greater<int>> q;
    int K;
    KthLargest(int k, vector<int>& nums):K(k){
        for(auto i:nums){
            add(i);
        }
    }
    
    int add(int val) {
        if(q.size()<K){
            q.push(val);
        }
        else if(val>q.top()){
            q.pop();
            q.push(val);
        }
        return q.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
// @lc code=end

