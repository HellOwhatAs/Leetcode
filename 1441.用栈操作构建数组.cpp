/*
 * @lc app=leetcode.cn id=1441 lang=cpp
 *
 * [1441] 用栈操作构建数组
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ret;
        int i=0;
        for(int num=1;num<=n;++num){
            if(num==target[i]){
                ret.push_back("Push");
                ++i;
                if(i==target.size())break;
            }
            else{
                ret.push_back("Push");
                ret.push_back("Pop");
            }
        }
        return ret;
    }
};
// @lc code=end

