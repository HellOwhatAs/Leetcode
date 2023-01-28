/*
 * @lc app=leetcode.cn id=993 lang=cpp
 *
 * [993] 二叉树的堂兄弟节点
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
class Solution {
public:
    int depth(TreeNode* root, int val) {
        if(root==nullptr)return -1;
        if(root->val == val)return 0;
        int tmp = depth(root->left, val);
        if(tmp != -1) return tmp+1;
        tmp = depth(root->right, val);
        if(tmp != -1) return tmp+1;
        return -1;
    }
    TreeNode* father(TreeNode* root, int val){
        if(root==nullptr)return nullptr;
        TreeNode* ret = nullptr;
        if(root->left!=nullptr){
            if(root->left->val == val)return root;
            ret = father(root->left, val);
            if(ret != nullptr)return ret;
        }
        if(root->right!=nullptr){
            if(root->right->val == val)return root;
            ret = father(root->right, val);
            if(ret != nullptr)return ret;
        }
        return nullptr;

    }
    bool isCousins(TreeNode* root, int x, int y) {
        return depth(root, x) == depth(root, y) && father(root, x) != father(root, y);
    }
};
// @lc code=end

