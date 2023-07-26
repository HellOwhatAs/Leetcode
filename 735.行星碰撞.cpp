/*
 * @lc app=leetcode.cn id=735 lang=cpp
 *
 * [735] 行星碰撞
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> s;
        for(auto i: asteroids) {
            mylabel:
            if(s.empty()) s.push_back(i);
            else{
                if(!(s.back() > 0 && i < 0)){
                    s.push_back(i);
                    continue;
                }
                if(s.back() > -i) continue;
                else if (s.back() < -i){
                    s.pop_back();
                    goto mylabel;
                }
                else s.pop_back();
            }
        }
        return s;
    }
};
// @lc code=end

