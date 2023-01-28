/*
 * @lc app=leetcode.cn id=590 lang=cpp
 *
 * [590] N 叉树的后序遍历
 */
#include<vector>
using namespace std;
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    void postorder(Node* root, vector<int>& ret) {
        if(root == nullptr)return;
        for(auto i:root->children){
            postorder(i, ret);
        }
        ret.push_back(root->val);
    }
    vector<int> postorder(Node* root) {
        vector<int> ret;
        postorder(root, ret);
        return ret;
    }
};
// @lc code=end

