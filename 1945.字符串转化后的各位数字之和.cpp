/*
 * @lc app=leetcode.cn id=1945 lang=cpp
 *
 * [1945] 字符串转化后的各位数字之和
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int getLucky(string s, int k) {
        int ret=0, tmp;
        for(auto c:s){
            ret+=(c-'a'+1)%10 + (c-'a'+1)/10;
        }
        for(int i=1;i<k;++i){
            tmp=0;
            while(ret){
                tmp+=ret%10;
                ret/=10;
            }
            ret=tmp;
        }
        return ret;
    }
};
// @lc code=end

