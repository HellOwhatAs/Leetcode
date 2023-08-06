/*
 * @lc app=leetcode.cn id=630 lang=cpp
 *
 * [630] 课程表 III
 */

// @lc code=start
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        sort(courses.begin(), courses.end(), [&](const vector<int>& a, const vector<int>& b){return a[1] < b[1];});
        priority_queue<int> selected;
        int now = 0;
        for(auto& duration_lastDay: courses){
            auto duration = duration_lastDay.front(), lastDay = duration_lastDay.back();
            if(now + duration <= lastDay){
                selected.push(duration);
                now += duration;
            }
            else if(!selected.empty() && selected.top() > duration && now + duration - selected.top() <= lastDay){
                now -= selected.top(); selected.pop();
                now += duration;
                selected.push(duration);
            }
        }
        return selected.size();
    }
};
// @lc code=end

