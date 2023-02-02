/*
 * @lc app=leetcode.cn id=897 lang=cpp
 *
 * [897] 递增顺序搜索树
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
    TreeNode* midorder(TreeNode *arr, TreeNode* root) {
        if(root == nullptr) return arr;
        arr = midorder(arr, root -> left);
        arr -> right = new TreeNode(root -> val);
        arr = arr -> right;
        return midorder(arr, root -> right);
    }
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* ret = new TreeNode(0);
        midorder(ret, root);
        return ret -> right;
    }
};
// @lc code=end

