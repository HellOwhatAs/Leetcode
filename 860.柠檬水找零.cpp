/*
 * @lc app=leetcode.cn id=860 lang=cpp
 *
 * [860] 柠檬水找零
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int c5 = 0, c10 = 0;
        for(auto i: bills){
            switch (i) {
                case 5:
                    ++c5;
                break;
                case 10:
                    if(c5){
                        --c5;
                        ++c10;
                    }
                    else return false;
                break;
                case 20:
                    if(c10 && c5){
                        --c5;
                        --c10;
                    }
                    else if(c5 >= 3) c5 -= 3;
                    else return false;
            }
        }
        return true;
    }
};
// @lc code=end

