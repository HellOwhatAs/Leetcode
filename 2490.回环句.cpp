/*
 * @lc app=leetcode.cn id=2490 lang=cpp
 *
 * [2490] 回环句
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    bool isCircularSentence(string sentence) {
        if(sentence.front() != sentence.back())return false;
        for(int i=1; i<sentence.length(); ++i){
            if(sentence[i] == ' '){
                if(sentence[i - 1] != sentence[i + 1])return false;
            }
        }
        return true;
    }
};
// @lc code=end

