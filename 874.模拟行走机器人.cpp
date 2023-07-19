/*
 * @lc app=leetcode.cn id=874 lang=cpp
 *
 * [874] 模拟行走机器人
 */

// @lc code=start
#include<vector>
#include<unordered_set>
using namespace std;
class Solution {
public:
    template<class T1, class T2>
    struct hash_pair{
        int operator()(const pair<T1, T2>& x) const {
            return (x.first) ^ (x.second);
        }
    };
    void turn(char& direction, int code){
        if(code == -2){
            switch (direction) {
                case '^': direction = '<'; return;
                case '<': direction = 'v'; return;
                case 'v': direction = '>'; return;
                case '>': direction = '^'; return;
            }
        }
        if(code == -1){
            switch (direction) {
                case '^': direction = '>'; return;
                case '>': direction = 'v'; return;
                case 'v': direction = '<'; return;
                case '<': direction = '^'; return;
            }
        }
        throw code;
    }
    void decode(char direction, int& dx, int& dy){
        switch (direction) {
            case '^': dx = 0, dy = 1; return;
            case 'v': dx = 0, dy = -1; return;
            case '<': dx = -1, dy = 0; return;
            case '>': dx = 1, dy = 0; return;
            default: throw direction;
        }
    }
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<pair<int, int>, hash_pair<int, int>> obs;
        for(auto& item: obstacles){
            obs.insert({item[0], item[1]});
        }
        int x = 0, y = 0, dx = 0, dy = 1, ret = 0;
        char direction = '^';
        for(auto cmd: commands){
            if(cmd < 0){
                turn(direction, cmd);
                decode(direction, dx, dy);
            }
            else{
                for(int _=0; _<cmd; ++_){
                    pair<int, int> tmp = {x + dx, y + dy};
                    if(obs.count(tmp))break;
                    x += dx;
                    y += dy;
                }
            }
            ret = max(ret, x*x + y*y);
        }
        return ret;
    }
};
// @lc code=end

