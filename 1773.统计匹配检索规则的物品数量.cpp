/*
 * @lc app=leetcode.cn id=1773 lang=cpp
 *
 * [1773] 统计匹配检索规则的物品数量
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int ret=0,ind;
        switch (ruleKey[0]){
            case 't':
                ind=0;
                break;
            case 'c':
                ind=1;
                break;
            default:
                ind=2;
                break;
        }
        for(auto&i:items){
            if(i[ind]==ruleValue)++ret;
        }
        return ret;
    }
};
// @lc code=end

