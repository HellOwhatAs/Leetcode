/*
 * @lc app=leetcode.cn id=415 lang=cpp
 *
 * [415] 字符串相加
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string addStrings(string num1, string num2) {
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        if(num1.size() < num2.size())num1.swap(num2);
        for(int i=0; i<num2.size(); ++i){
            num1[i] += num2[i] - '0';
        }
        int i = 0, tmp = 0;
        while(i < num1.size() || num1[i] > '9'){
            num1[i] += tmp;
            tmp = 0;
            if(num1[i] > '9'){
                tmp = (num1[i]- '0')/10;
                num1[i] = (num1[i]- '0')%10 + '0';
            }
            ++i;
        }
        if(tmp)num1.push_back(tmp + '0');
        reverse(num1.begin(), num1.end());
        return num1;
    }
};
// @lc code=end

