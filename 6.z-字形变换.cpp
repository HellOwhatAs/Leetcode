/*
 * @lc app=leetcode.cn id=6 lang=cpp
 *
 * [6] Z 字形变换
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
        string *a=new string[numRows];
        int ind=0,l=s.size();
        while(ind<l){
            for(int i=0;i<numRows&&ind<l;++i,++ind){
                a[i].push_back(s[ind]);
            }
            for(int i=numRows-2;i>0&&ind<l;--i,++ind){
                a[i].push_back(s[ind]);
            }
        }
        for(int i=1;i<numRows;++i){
            a[0].append(a[i].c_str());
        }
        return a[0];
    }
};
// @lc code=end

