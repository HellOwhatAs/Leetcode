/*
 * @lc app=leetcode.cn id=722 lang=cpp
 *
 * [722] 删除注释
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    const string& new_state(char& state, char c){
        if(state == '/'){
            if(c == '/'){
                state = c;
                return "//";
            }
            else if(c == '*'){
                state = c;
                return "/*";
            }
        }
        else if(state == '*'){
            if(c == '/'){
                state = c;
                return "*/";
            }
        }
        state = c;
        return "";
    }
    vector<string> removeComments(vector<string>& source) {
        vector<string> ret;
        char state = 0;
        bool multi_line = false;
        for(auto& line: source){
            if(!multi_line && (ret.empty() || !ret.back().empty())) ret.push_back("");
            for(char c: line){
                const string& token = new_state(state, c);
                if(!multi_line && token == "//"){
                    ret.back().pop_back();
                    state = 0;
                    break;
                }
                if(!multi_line && token == "/*"){
                    ret.back().pop_back();
                    state = 0;
                    multi_line = true;
                    continue;
                }
                if(multi_line && token == "*/"){
                    state = 0;
                    multi_line = false;
                    continue;
                }
                if(!multi_line) ret.back().push_back(c);
            }
        }
        return ret;
    }
};
// @lc code=end

