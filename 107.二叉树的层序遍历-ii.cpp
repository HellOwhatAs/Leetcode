/*
 * @lc app=leetcode.cn id=107 lang=cpp
 *
 * [107] 二叉树的层序遍历 II
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include<vector>
#include<queue>
using namespace std;
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if(root==nullptr)return {};
        vector<vector<int>> ret;
        vector<int> tmp;
        queue<TreeNode*> q1,q2;
        q1.push(root);
        ret.push_back({root->val});
        while(!q1.empty()){
            while(!q1.empty()){
                auto t=q1.front();q1.pop();
                if(t->left!=nullptr){
                    tmp.push_back(t->left->val);
                    q2.push(t->left);
                }
                if(t->right!=nullptr){
                    tmp.push_back(t->right->val);
                    q2.push(t->right);
                }
            }
            q1.swap(q2);
            ret.push_back({});
            ret.back().swap(tmp);
        }
        ret.pop_back();
        reverse(ret.begin(),ret.end());
        return ret;
    }
};
// @lc code=end

