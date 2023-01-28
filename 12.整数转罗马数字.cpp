/*
 * @lc app=leetcode.cn id=12 lang=cpp
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string d[13]={"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int a[13]={1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string intToRoman(int num) {
        string ret;
        int i=0;
        while(num){
            while(num>=a[i]){
                ret+=d[i];
                num-=a[i];
            }
            ++i;
        }
        return ret;
    }
};
// @lc code=end

