/*
 * @lc app=leetcode.cn id=1769 lang=cpp
 *
 * [1769] 移动所有球到每个盒子所需的最小操作数
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> ret(boxes.size(),0),bolls;
        for(int i=0;i<boxes.size();++i){
            if(boxes[i]=='1')bolls.push_back(i);
        }
        for(int i=0;i<boxes.size();++i){
            for(auto&j:bolls){
                ret[i]+=abs(j-i);
            }
        }
        return ret;
    }
};
// @lc code=end

