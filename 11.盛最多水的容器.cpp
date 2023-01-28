/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
public:
    int area(const vector<int>& height,int l,int r){
        return (r-l)*min(height[l],height[r]);
    }
    int maxArea(vector<int>& height) {
        int s=0,e=height.size()-1,v;
        bool flag;
        int ms=s,me=e,mv=area(height,s,e);
        while(s<e-1){
            flag=0;
            if(height[s]>height[e]){if(height[e--]<height[e])flag=1;}
            else if(height[s++]<height[s])flag=1;
            if(flag){
                v=(e-s)*min(height[s],height[e]);
                if(v>mv){
                    ms=s;
                    me=e;
                    mv=v;
                }
            }
        }
        return mv;
    }
};
// @lc code=end

