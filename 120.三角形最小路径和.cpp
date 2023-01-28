/*
 * @lc app=leetcode.cn id=120 lang=cpp
 *
 * [120] 三角形最小路径和
 */

// @lc code=start
#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    vector<vector<int>>* a;
    unordered_map<int,int> dd;
    int func(int x,int y){
        int h=x*1000+y;
        if(dd.count(h))return dd[h];
        if(y==a->size()-1)return dd[h]=(*a)[y][x];
        return dd[h]=(*a)[y][x]+min(func(x,y+1),func(x+1,y+1));
    }
    int minimumTotal(vector<vector<int>>& triangle) {
        a=&triangle;
        dd.clear();
        return func(0,0);
    }
};
// @lc code=end

