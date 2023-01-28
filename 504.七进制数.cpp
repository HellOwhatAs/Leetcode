/*
 * @lc app=leetcode.cn id=504 lang=cpp
 *
 * [504] 七进制数
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string convertToBase7(int num) {
        string ret;
        bool flag=0;
        if(num<0){
            num=-num;
            flag=1;
        }
        while(num){
            ret.push_back(num%7+'0');
            num/=7;
        }
        if(flag)ret.push_back('-');
        reverse(ret.begin(), ret.end());
        if(ret.empty())ret.push_back('0');
        return ret;
    }
};
// @lc code=end
