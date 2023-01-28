/*
 * @lc app=leetcode.cn id=98 lang=cpp
 *
 * [98] 验证二叉搜索树
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
#include<climits>
class Solution {
public:
    bool valid(TreeNode* root,long less,long large){
        if(root->val>=less||root->val<=large)return false;
        if(root->left){
            if(!valid(root->left,root->val,large))return false;
        }
        if(root->right){
            if(!valid(root->right,less,root->val))return false;
        }
        return true;
    }
    bool isValidBST(TreeNode* root) {
        return valid(root,LONG_MAX,LONG_MIN);
    }
};
// @lc code=end

