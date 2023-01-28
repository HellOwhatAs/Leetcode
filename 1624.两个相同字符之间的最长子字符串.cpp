/*
 * @lc app=leetcode.cn id=1624 lang=cpp
 *
 * [1624] 两个相同字符之间的最长子字符串
 */

// @lc code=start
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int prev[26]={0},max_len=-1,tmp,key;
        for(int i=0;i<s.size();++i){
            key=s[i]-'a';
            if(prev[key])max_len=max(max_len,i-prev[key]);
            else prev[key]=i+1;
        }
        return max_len;
    }
};
// @lc code=end

