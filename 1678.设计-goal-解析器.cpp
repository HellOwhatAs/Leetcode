/*
 * @lc app=leetcode.cn id=1678 lang=cpp
 *
 * [1678] 设计 Goal 解析器
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string interpret(string command) {
        string ret;
        int n=command.size();
        for(int i=0;i<n;++i){
            if(command[i]=='G')ret.push_back('G');
            else{
                ++i;
                if(command[i]==')')ret.push_back('o');
                else{
                    i+=2;
                    ret.append("al");
                }
            }
        }
        return ret;
    }
};
// @lc code=end

