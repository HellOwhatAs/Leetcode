/*
 * @lc app=leetcode.cn id=809 lang=cpp
 *
 * [809] 情感丰富的文字
 */

// @lc code=start
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    static vector<pair<char,int>> func(const string&x){
        vector<pair<char,int>> ret;
        for(auto i:x){
            if(ret.empty() || ret.back().first!=i)ret.push_back({i,1});
            else ++ret.back().second;
        }
        return ret;
    }
    int expressiveWords(string s, vector<string>& words) {
        auto fs=func(s);
        int ret=0, lfs=fs.size();
        for(auto&word:words){
            auto fword=func(word);
            if(fword.size()!=lfs)continue;
            for(int i=0;i<lfs;++i){
                if(fs[i].first!=fword[i].first ||
                   fs[i].second!=fword[i].second && fs[i].second < 3 ||
                   fs[i].second < fword[i].second){
                    --ret;
                    break;
                }
            }
            ++ret;
        }
        return ret;
    }
};
// @lc code=end

// "dddiiiinnssssssoooo"\n["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]