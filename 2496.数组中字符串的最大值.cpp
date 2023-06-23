/*
 * @lc app=leetcode.cn id=2496 lang=cpp
 *
 * [2496] 数组中字符串的最大值
 */

// @lc code=start
#include<vector>
#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    bool isdigit(const string& str){
        for(auto c: str){
            if('0' <=c && c <= '9')continue;
            else return false;
        }
        return true;
    }
    int maximumValue(vector<string>& strs) {
        int ret = 0;
        for(auto & str : strs) {
            if(isdigit(str)){
                ret = max(ret, stoi(str));
            }
            else ret = max(ret, (int)str.size());
        }
        return ret;
    }
};
// @lc code=end

int main(){
    cout << Solution().maximumValue(vector<string>({"alic3","bob","3","4","00000"}));
    return 0;
}