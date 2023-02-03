/*
 * @lc app=leetcode.cn id=1145 lang=cpp
 *
 * [1145] 二叉树着色游戏
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
    TreeNode *treefind(TreeNode *root, int val) {
        if(root == nullptr || root -> val == val) return root;
        TreeNode *tmp = treefind(root -> left, val);
        if(tmp != nullptr) return tmp;
        return treefind(root -> right, val);
    }
    int treesize(TreeNode *root) {
        if(root == nullptr) return 0;
        return treesize(root -> left) + treesize(root -> right) + 1;
    }
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        if(root -> val == x) return (treesize(root -> left) > n / 2) || (treesize(root -> right) > n / 2);
        else{
            TreeNode *red = treefind(root, x);
            return (treesize(red) <= n / 2) || (treesize(red -> left) > n / 2) || (treesize(red -> right) > n / 2);
        }
    }
};
// @lc code=end

