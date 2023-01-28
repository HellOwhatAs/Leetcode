/*
 * @lc app=leetcode.cn id=940 lang=cpp
 *
 * [940] 不同的子序列 II
 */

// @lc code=start
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    int distinctSubseqII(string s) {
        long long tmp, ret=0, last[26]={0};
        for(int i=0;i<s.size();++i){
            tmp=1;
            for(int k=0;k<26;++k){
                tmp=(tmp+last[k])%1000000007;
            }
            last[s[i]-'a']=tmp;
        }
        for(int k=0;k<26;++k){
            ret=(ret+last[k])%1000000007;
        }
        return ret;
    }
};
// @lc code=end

