/*
 * @lc app=leetcode.cn id=1832 lang=cpp
 *
 * [1832] 判断句子是否为全字母句
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    bool checkIfPangram(string sentence) {
        int ret=0;
        for(auto c:sentence){
            ret |= 1<<(c-'a');
        }
        return ret==((1<<26)-1);
    }
};
// @lc code=end

