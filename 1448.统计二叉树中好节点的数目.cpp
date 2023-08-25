/*
 * @lc app=leetcode.cn id=1448 lang=cpp
 *
 * [1448] 统计二叉树中好节点的数目
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
#include<utility>

class Solution {
public:
    int goodNodes(TreeNode* root, int _max = INT_MIN) {
        if(root == nullptr) return 0;
        int ret = (root->val >= _max)? 1: 0, tmp = std::max(root->val, _max);
        return ret + goodNodes(root->left, tmp) + goodNodes(root->right, tmp);
    }
};
// @lc code=end

