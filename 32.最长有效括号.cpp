/*
 * @lc app=leetcode.cn id=32 lang=cpp
 *
 * [32] 最长有效括号
 */

// @lc code=start
#include<stack>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
class Solution {
public:
    // int longestValidParentheses_old(string s) {
    //     int l=s.size();
    //     if(!l)return 0;
    //     int lcount[30001],rcount[30001],max_len=0;
    //     lcount[0]=rcount[0]=0;
    //     for(int i=0;i<l;++i){
    //         lcount[i+1]=lcount[i];
    //         rcount[i+1]=rcount[i];
    //         if(s[i]=='(')++lcount[i+1];
    //         else ++rcount[i+1];
    //     }
    //     if(lcount[l]==0||rcount[l]==0)return 0;
    //     for(int _start=0;_start<l;++_start){
    //         int _end=_start+1;
    //         while(_end<=l){
    //             int tmp=lcount[_end]-lcount[_start]-(rcount[_end]-rcount[_start]);
    //             if(tmp<0)break;
    //             if(tmp==0)max_len=max(max_len,_end-_start);
    //             ++_end;
    //         }
    //     }
    //     return max_len;
    // }
    int longestValidParentheses(string s) {
        stack<int> lpart;
        vector<int> error_pos;
        for(int i=0;i<s.size();++i){
            if(s[i]=='(')lpart.push(i);
            else{
                if(lpart.empty())error_pos.push_back(i);
                else{
                    lpart.pop();
                }
            }
        }
        while(!lpart.empty()){
            error_pos.push_back(lpart.top());lpart.pop();
        }
        if(error_pos.empty())return s.size();
        sort(error_pos.begin(),error_pos.end());
        int ret=0;
        ret=max(error_pos[0],ret);
        ret=max(ret,int(s.size())-1-error_pos[error_pos.size()-1]);
        for(int i=1;i<error_pos.size();++i){
            ret=max(ret,error_pos[i]-1-error_pos[i-1]);
        }
        return ret;
    }
};
// @lc code=end
//  s   e
// [0,1,2]
// [0,1,2,2]
// [0,0,0,1]