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
    int token_end(const string& expression, int start) {
        for(int i=start; i<expression.size(); ++i){
            if(expression[i] == ' ' || expression[i] == '(' || expression[i] == ')')return i-1;
        }
        return expression.size()-1;
    }
    struct expr{
        bool is_leaf;
        string val;
        vector<expr*> childs;
    };
    int eval(const expr* root) {
        if(root->is_leaf){
            if(root->val[0] == '-' || root->val[0] >= '0' && root->val[0] <= '9') return stoi(root->val);
            return gbl[root->val];
        }
        int ret = 0;
        if(root->val == "let"){
            unordered_map<string, int> nonlocals;
            vector<string> locals;
            for(int i=1; i<root->childs.size(); i+=2){
                auto & vname = root->childs[i-1]->val;
                if(gbl.count(vname)) nonlocals[vname] = gbl[vname];
                else locals.push_back(vname);
                gbl[vname] = eval(root->childs[i]);
            }
            ret = eval(root->childs.back());
            for(auto& [k, v]: nonlocals){
                gbl[k] = v;
            }
            for(auto& k: locals) gbl.erase(k);
        }
        else if(root->val == "add"){
            for(auto& i: root->childs){
                ret += eval(i);
            }
        }
        else if(root->val == "mult"){
            ret = 1;
            for(auto& i: root->childs){
                ret *= eval(i);
            }
        }
        else throw root->val + " not implemented";
        return ret;
    }
    void free(expr* root) {
        for(auto& p: root->childs)free(p);
        delete root;
    }
    int evaluate(const string& expression) {
        stack<expr*> s;
        int i = 0, tmp;
        while(i < expression.size()){
            if(expression[i] == ' ') ++i;
            else if(expression[i] == '('){
                s.push(nullptr);
                ++i;
            }
            else if(expression[i] == ')'){
                expr* p = new expr({false});
                while(s.top() != nullptr){
                    p->childs.push_back(s.top());
                    s.pop();
                }
                s.pop();
                p->val = p->childs.back()->val;
                delete p->childs.back();
                p->childs.pop_back();
                reverse(p->childs.begin(), p->childs.end());
                s.push(p);
                ++i;
            }
            else{
                tmp = token_end(expression, i);
                s.push(new expr({true, expression.substr(i, tmp - i + 1)}));
                i = tmp + 1;
            }
        }
        tmp = eval(s.top());
        free(s.top());
        return tmp;
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