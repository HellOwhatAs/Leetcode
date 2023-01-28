/*
 * @lc app=leetcode.cn id=854 lang=cpp
 *
 * [854] 相似度为 K 的字符串
 */

// @lc code=start
#include<string>
#include<climits>
#include<unordered_map>
using namespace std;
unordered_map<string,int> dd;
class Solution {
public:
    int func(const string&s1, const string&s2){
        if(dd.count(s1))return dd[s1];
        if(s1==s2){
            dd[s1]=0;
            return 0;
        }
        int ret=INT_MAX,tmp;
        string subs1=s1.substr(1),subs2=s2.substr(1);
        if(s1[0]==s2[0])ret=func(subs1,subs2);
        else{
            for(int i=1;i<s1.size();++i){
                if(s1[i]==s2[0]){
                    subs1[i-1]=s1[0];
                    tmp=func(subs1,subs2);
                    subs1[i-1]=s2[0];
                    ret=min(ret,1+tmp);
                    if(tmp==0)break;
                }
            }
        }
        dd[s1]=ret;
        return ret;
    }
    int kSimilarity(string s1, string s2) {
        dd.clear();
        int ret=func(s1,s2);
        return ret;
    }
};
// @lc code=end

// "accbadbbacadcdedaebc"
// "caeacbbacddceacadbbd"