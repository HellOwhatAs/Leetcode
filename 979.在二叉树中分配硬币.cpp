/*
 * @lc app=leetcode.cn id=979 lang=cpp
 *
 * [979] 在二叉树中分配硬币
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
#include<vector>
using namespace std;
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
    // Return (size, sum(val))
    int ret;
    pair<int, int> TreeSize(TreeNode* root) {
        if(root == nullptr) return {0, 0};
        auto left = TreeSize(root->left), right = TreeSize(root->right);
        int Size = left.first + right.first + 1, SumVal = left.second + right.second + root->val;
        ret += abs(Size - SumVal);
        return {Size, SumVal};
    }
    int distributeCoins(TreeNode* root) {
        ret = 0;
        TreeSize(root);
        return ret;
    }
};
// @lc code=end

