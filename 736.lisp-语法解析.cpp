/*
 * @lc app=leetcode.cn id=736 lang=cpp
 *
 * [736] Lisp 语法解析
 */

// @lc code=start
#include<vector>
#include<string>
#include<stack>
#include<unordered_map>
using namespace std;

class Solution {
public:
    unordered_map<string, int> gbl;
    int find_right(const string& expression, int left) {
        int pure_left = 1;
        ++left;
        while(left < expression.size()){
            if(expression[left] == '(') ++pure_left;
            else if(expression[left] == ')') --pure_left;
            if(pure_left == 0) return left;
            ++left;
        }
        throw "no ')' match";
    }
    int literal_find_end(const string& expression, int start) {
        for(int i=start; i<expression.size(); ++i){
            if(expression[i] == ' ' || expression[i] == '(' || expression[i] == ')')return i-1;
        }
        return expression.size()-1;
    }
    int find_end(const string& expression, int start) {
        if(expression[start] == '(')return find_right(expression, start);
        return literal_find_end(expression, start);
    }
    int evaluate(const string& expression, int start = 0, int end = -1) {
        if(end == -1) end = expression.size() - 1;
        int ret;
        if(expression[start] == '('){
            if(expression[start + 1] == 'l'){ // let
                int i = start + 5;
                vector<pair<int, int>> elems;
                while(i < end){
                    elems.push_back({i, find_end(expression, i)});
                    i = elems.back().second + 2;
                }
                unordered_map<string, int> tmp_gbl;
                for(int j=0; j<elems.size(); j+=2){
                    auto [vs, ve] = elems[j];
                    if(j + 1 < elems.size()){
                        auto && vname = expression.substr(vs, ve - vs + 1);
                        tmp_gbl[vname] = gbl[vname];
                        auto [es, ee] = elems[j+1];
                        gbl[vname] = evaluate(expression, es, ee);
                    }
                    else{
                        ret = evaluate(expression, vs, ve);
                    }
                }
                for(auto& [k, v]: tmp_gbl){
                    gbl[k] = v;
                }
            }
            else if(expression[start + 1] == 'a'){ // add
                int i = start + 5, a, b, tmp = find_end(expression, i);
                a = evaluate(expression, i, tmp);
                b = evaluate(expression, tmp + 2, find_end(expression, tmp + 2));
                ret = a + b;
            }
            else{ // expression[start + 1] == 'm' // mult
                int i = start + 6, a, b, tmp = find_end(expression, i);
                a = evaluate(expression, i, tmp);
                b = evaluate(expression, tmp + 2, find_end(expression, tmp + 2));
                ret = a * b;
            }
        }
        else if(expression[start] == '-' || expression[start] >= '0' && expression[start] <= '9'){
            ret = stoi(expression.substr(start, end - start + 1));
        }
        else{
            ret = gbl[expression.substr(start, end - start + 1)];
        }
        return ret;
    }
};
// @lc code=end

/*
(let 
    x 2 
    (mult 
        x 
        (let 
            x 3 
            y 4 
            (add x y)
        )
    )
)
*/