/*
 * @lc app=leetcode.cn id=1768 lang=cpp
 *
 * [1768] 交替合并字符串
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ret(word1.size()+word2.size(),'\0');
        if(word1.size()<=word2.size()){
            for(int i=0;i<word1.size();++i){
                ret[i*2]=word1[i];
            }
            int j=0;
            for(int i=0;i<ret.size();++i){
                if(ret[i]==0){
                    ret[i]=word2[j];
                    ++j;
                }
            }
        }
        else{
            for(int i=0;i<word2.size();++i){
                ret[i*2+1]=word2[i];
            }
            int j=0;
            for(int i=0;i<ret.size();++i){
                if(ret[i]==0){
                    ret[i]=word1[j];
                    ++j;
                }
            }
        }
        return ret;
    }
};
// @lc code=end

