/*
 * @lc app=leetcode.cn id=543 lang=cpp
 *
 * [543] 二叉树的直径
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
    int longest(TreeNode* root, int* ret) {
        if(root == nullptr)return 0;
        int ll = longest(root->left, ret), lr = longest(root->right, ret);
        if(ll+lr > *ret)*ret=ll+lr;
        return max(ll, lr) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int ret = 0;
        longest(root, &ret);
        return ret;
    }
};
// @lc code=end

