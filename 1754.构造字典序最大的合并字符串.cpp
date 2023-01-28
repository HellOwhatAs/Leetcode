/*
 * @lc app=leetcode.cn id=1754 lang=cpp
 *
 * [1754] 构造字典序最大的合并字符串
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    string largestMerge(string word1, string word2) {
        string ret;
        int s1=0, s2=0;
        while(s1<word1.size() || s2<word2.size()){
            if(strcmp(word1.c_str()+s1,word2.c_str()+s2)<0){
                ret.push_back(word2[s2++]);
            }
            else{
                ret.push_back(word1[s1++]);
            }
        }
        while(s1<word1.size()){
            ret.push_back(word1[s1++]);
        }
        while(s2<word2.size()){
            ret.push_back(word2[s2++]);
        }
        return ret;
    }
};
// @lc code=end
