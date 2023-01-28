/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len=0,_start=-1,d[256],tmp;
        for(int i=0;i<256;++i)d[i]=-1;
        for(int i=0;i<s.size();++i){
            _start=max(d[s[i]],_start);
            max_len=max(max_len,i-_start);
            d[s[i]]=i;
        }
        return max_len;
    }
};
// @lc code=end