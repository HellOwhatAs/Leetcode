/*
 * @lc app=leetcode.cn id=1779 lang=cpp
 *
 * [1779] 找到最近的有相同 X 或 Y 坐标的点
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int ret=-1,ret_value=INT_MAX, tmp;
        for(int i=0;i<points.size();++i){
            if((points[i][0]==x || points[i][1]==y) && (tmp=abs(x-points[i][0])+abs(y-points[i][1])) < ret_value){
                ret_value=tmp;
                ret=i;
            }
        }
        return ret;
    }
};
// @lc code=end

