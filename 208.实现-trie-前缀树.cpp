/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 */

// @lc code=start
#include<string>
#include<iostream>
using namespace std;

class Trie {
public:
    Trie* childs[26];
    bool leaf;
    Trie() {
        for(int i=0; i<26; ++i) childs[i] = nullptr;
        leaf = false;
    }

    ~Trie() {
        for(int i=0; i<26; ++i) {
            if(childs[i] != nullptr) {
                delete childs[i];
            }
        }
    }

    void insert(const string& word, int start = 0) {
        if(start == word.size()){
            this->leaf = true;
            return;
        }
        auto idx = word[start] - 'a';
        if(this->childs[idx] == nullptr)
            this->childs[idx] = new Trie;
        this->childs[idx]->insert(word, start + 1);
        
    }
    
    bool search(const string& word, int start = 0) {
        if(start == word.size()) return this->leaf;
        auto idx = word[start] - 'a';
        if(this->childs[idx] == nullptr)
            return false;
        return this->childs[idx]->search(word, start + 1);
    }
    
    bool startsWith(const string& prefix, int start = 0) {
        if(start == prefix.size()) return true;
        auto idx = prefix[start] - 'a';
        if(this->childs[idx] == nullptr)
            return false;
        return this->childs[idx]->startsWith(prefix, start + 1);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end

