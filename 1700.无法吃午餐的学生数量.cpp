/*
 * @lc app=leetcode.cn id=1700 lang=cpp
 *
 * [1700] 无法吃午餐的学生数量
 */

// @lc code=start
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        reverse(sandwiches.begin(),sandwiches.end());
        queue<int> ss;
        for(auto i:students)ss.push(i);
        int count=0;
        while(count<ss.size()){
            // cout<<count<<'\n';
            if(ss.front()==sandwiches.back()){
                ss.pop();
                sandwiches.pop_back();
                count=0;
            }
            else{
                ss.push(ss.front());ss.pop();
                ++count;
            }
        }
        return ss.size();
    }
};
// @lc code=end

