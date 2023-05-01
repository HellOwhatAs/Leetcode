/*
 * @lc app=leetcode.cn id=1376 lang=cpp
 *
 * [1376] 通知所有员工所需的时间
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    struct Node{
        int val, time;
        vector<int> childs;
    };
    int func(Node* data, int idx) {
        int ret = 0;
        for(auto i: data[idx].childs) {
            ret = max(ret, func(data, i));
        }
        return ret + data[idx].time;
    }
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        Node* data = new Node[n];
        for(int i = 0; i < n; ++i) {
            data[i].val = i;
            data[i].time = informTime[i];
            if(i != headID)data[manager[i]].childs.push_back(i);
        }
        return func(data, headID);
    }
};
// @lc code=end

