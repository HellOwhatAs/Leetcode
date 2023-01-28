/*
 * @lc app=leetcode.cn id=14 lang=cpp
 *
 * [14] 最长公共前缀
 */

// @lc code=start
#include<climits>
#include<string>
using namespace std;
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int ret=0,min_len=INT_MAX;
        char tmp;bool flag;
        for(auto&i:strs)min_len=min(min_len,(int)i.size());
        for(int i=0;i<min_len;++i){
            tmp=strs[0][i];
            flag=0;
            for(int j=1;j<strs.size();++j){
                if(strs[j][i]!=tmp){
                    flag=1;
                    break;
                }
            }
            if(flag)return strs[0].substr(0,i);
        }
        return strs[0].substr(0,min_len);
    }
};
// @lc code=end

