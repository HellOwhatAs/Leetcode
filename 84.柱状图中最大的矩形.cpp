/*
 * @lc app=leetcode.cn id=84 lang=cpp
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
#include<vector>
#include<stack>
using namespace std;
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.insert(heights.begin(),0);
        heights.push_back(0);
        stack<int> s;
        int ret=0,tmp;
        for(int i=0;i<heights.size();++i){
            while((!s.empty())&&heights[s.top()]>heights[i]){
                tmp=s.top();s.pop();
                ret=max(ret,(i-s.top()-1)*heights[tmp]);
            }
            s.push(i);
        }
        return ret;
    }
};
// @lc code=end

[0,0,0,0,0,0]
[1,2,3,4,5,6]