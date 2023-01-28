/*
 * @lc app=leetcode.cn id=921 lang=cpp
 *
 * [921] 使括号有效的最少添加
 */

// @lc code=start
#include<stack>
#include<string>
using namespace std;
class Solution {
public:
    int minAddToMakeValid(string s) {
        int count=0,ret=0;
        for(auto&i:s){
            if(i=='(')++count;
            else{
                if(count==0)++ret;
                else --count;
            }
        }
        return ret+count;
    }
};
// @lc code=end

