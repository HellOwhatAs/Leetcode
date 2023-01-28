/*
 * @lc app=leetcode.cn id=114 lang=cpp
 *
 * [114] 二叉树展开为链表
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
#include<iostream>
using namespace std;
class Solution {
public:
    TreeNode*&firstorder(TreeNode* root){
        if(root->left!=nullptr){
            if(root->right==nullptr){
                auto&tmp=firstorder(root->left);
                swap(root->left,root->right);
                return tmp;
            }
            TreeNode*tmp;
            firstorder(root->left)=root->right;
            tmp=root->right;
            root->right=root->left;
            root->left=nullptr;
            return firstorder(tmp);
        }
        if(root->right==nullptr)return root->right;
        return firstorder(root->right);
    }
    void flatten(TreeNode* root) {
        if(root==nullptr)return;
        firstorder(root)=nullptr;
    }
};
// @lc code=end

