/*
 * @lc app=leetcode.cn id=1796 lang=cpp
 *
 * [1796] 字符串中第二大的数字
 */

// @lc code=start
#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    int secondHighest(string s) {
        bool has[10]={0},flag=0;
        for(auto c:s){
            if('0'<=c && c<='9')has[c-'0']=1;
        }
        for(int i=9;i>=0;--i){
            if(has[i]){
                if(flag)return i;
                flag=1;
            }
        }
        return -1;
    }
};
// @lc code=end

