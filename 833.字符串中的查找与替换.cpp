/*
 * @lc app=leetcode.cn id=833 lang=cpp
 *
 * [833] 字符串中的查找与替换
 */

// @lc code=start
#include<vector>
#include<string>
#include<tuple>
#include<algorithm>
#include<iostream>
using namespace std;

class Solution {
public:
    string findReplaceString(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
        int k = indices.size();
        vector<tuple<int, string*, string*>> zip;
        for(int i=0; i<k; ++i){
            zip.push_back({indices[i], &sources[i], &targets[i]});
        }
        sort(zip.begin(), zip.end());
        string pre = s.substr(0, get<0>(zip.front()));
        vector<string> ss;

        for(int i=0; i<k; ++i){
            ss.push_back(s.substr(get<0>(zip[i]), (i+1<k? get<0>(zip[i+1]) - get<0>(zip[i]): string::npos)));
        }

        for(int i=0; i<k; ++i){
            auto& tmp = zip[i];
            auto &source = *get<1>(tmp), &target = *get<2>(tmp);
            if(ss[i].substr(0, source.size()) == source){
                pre.append(target);
                pre.append(ss[i].substr(source.size()));
            }
            else pre.append(ss[i]);
        }
        return pre;
    }
};
// @lc code=end

