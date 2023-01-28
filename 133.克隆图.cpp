/*
 * @lc app=leetcode.cn id=133 lang=cpp
 *
 * [133] 克隆图
 */
#include<vector>
using namespace std;
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
#include<unordered_map>
#include<iostream>
class Solution {
public:
    unordered_map<int,Node*> allnodes,ret;
    void dfs(Node*node){
        if(allnodes.count(node->val))return;
        allnodes[node->val]=node;
        ret[node->val]=new Node(node->val);
        for(auto i:node->neighbors){
            dfs(i);
        }
    }
    Node* cloneGraph(Node* node) {
        if(node==nullptr)return nullptr;
        allnodes.clear();
        ret.clear();
        dfs(node);
        for(auto&i:allnodes){
            for(auto j:allnodes[i.first]->neighbors){
                ret[i.first]->neighbors.push_back(ret[j->val]);
            }
        }
        return ret[node->val];
    }
};
// @lc code=end

