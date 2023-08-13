/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:

    vector<int> feature(const string& s, int _start = 0, int _end = -1){
        if(_end == -1) _end = s.size();
        vector<int> ret(26, 0);
        for(int i=_start; i<_end; ++i) ++ret[s[i] - 'a'];
        return ret;
    }

    vector<int> findAnagrams(string s, string p) {
        int lenp = p.size(), tmp = s.size() - lenp + 1;
        if(s.size() < lenp) return {};
        auto feature_p = feature(p);
        auto feature_s = feature(s, 0, lenp);
        vector<int> ret;
        if(feature_s == feature_p) ret.push_back(0);
        for(int i=1; i<tmp; ++i){
            --feature_s[s[i-1] - 'a'];
            ++feature_s[s[i+lenp-1] - 'a'];
            if(feature_s == feature_p) ret.push_back(i);
        }
        return ret;
    }
};
// @lc code=end

