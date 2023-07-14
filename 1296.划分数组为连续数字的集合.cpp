/*
 * @lc app=leetcode.cn id=1296 lang=cpp
 *
 * [1296] 划分数组为连续数字的集合
 */

// @lc code=start
#include<map>
#include<vector>
using namespace std;
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        map<int, int> m;
        for(auto i:hand){
            if(m.count(i)) ++m[i];
            else m[i] = 1;
        }
        for(auto item:m){
            if(item.second == 0) continue;
            int tmp = item.first+groupSize;
            for(int i=item.first; i<tmp; ++i){
                if(!m.count(i) || m[i]<item.second) return false;
                m[i]-=item.second;
            }
        }
        
        return true;
    }
    bool isPossibleDivide(vector<int>& nums, int k) {
        return isNStraightHand(nums, k);
    }
};
// @lc code=end

