/*
 * @lc app=leetcode.cn id=139 lang=cpp
 *
 * [139] 单词拆分
 */

// @lc code=start
#include<vector>
#include<string>
#include<unordered_map>
using namespace std;

class Solution {
public:
    class Node{
    public:
        unordered_map<char, Node*> *next;
        bool is_leaf;
        Node(){
            is_leaf = false;
            next = new unordered_map<char, Node*>;    
        }
        Node(const vector<string>& init){
            is_leaf = false;
            next = new unordered_map<char, Node*>;
            for(auto& word: init) insert(word);
        }
        ~Node(){
            delete next;
        }
        void insert(const string& word, int start = 0){
            if(start == word.size()){
                is_leaf = true;
                return;
            }
            if(!next->count(word[start]))
                (*next)[word[start]] = new Node();
            (*next)[word[start]]->insert(word, start + 1);
        }
        Node* search(const string& pre, int start = 0){
            if(start == pre.size()) return this;
            if(next->count(pre[start])) return (*next)[pre[start]]->search(pre, start + 1);
            return nullptr;
        }
        Node* search(char pre){
            if(next->count(pre)) return (*next)[pre];
            return nullptr;
        }
        vector<string> extract(){
            vector<string> ret;
            string pre;
            __dfs(ret, pre);
            return ret;
        }
        void __dfs(vector<string>& output, string& pre){
            if(is_leaf) output.push_back(pre);
            for(auto item: *next){
                pre.push_back(item.first);
                (*next)[item.first]->__dfs(output, pre);
                pre.pop_back();
            }
        }
    };

    unordered_map<int, bool> cache;
    
    bool dfs(const string& s, Node* wd, int start){
        ///////////////////////
        if(cache.count(start)) return cache[start];
        ///////////////////////
        if(start == s.size()) {
            return cache[start] = true;
        }
        auto node = wd;
        for(int i=start; i<s.size(); ++i){
            node = node->search(s[i]);
            if(node == nullptr) break;
            if(node->is_leaf){
                if(dfs(s, wd, i + 1)) return cache[start] = true;;
            }
        }
        return cache[start] = false;
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        cache.clear();
        return dfs(s, new Node(wordDict), 0);
    }
};
// @lc code=end

