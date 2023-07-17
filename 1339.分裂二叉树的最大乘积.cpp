/*
 * @lc app=leetcode.cn id=1339 lang=cpp
 *
 * [1339] 分裂二叉树的最大乘积
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
#include<unordered_map>
class Solution {
public:
    long long int ret, root_sum, MOD = 1000000007;
    long long int TreeSum(TreeNode* root) {
        if (root == nullptr) return 0;
        return root->val = TreeSum(root->left) + TreeSum(root->right) + root->val;
    }
    void dfs(TreeNode* root){
        if(root == nullptr) return;
        long long int tmp, candidate;
        if(root->left != nullptr){
            tmp = root->left->val;
            candidate = (root_sum - tmp) * tmp;
            ret = std::max(ret, ((root_sum - tmp) * tmp));
            if(!(candidate <= ret && tmp < (root_sum - tmp)))
                dfs(root->left);
        }
        if(root->right != nullptr){
            tmp = root->right->val;
            ret = std::max(ret, ((root_sum - tmp) * tmp));
            if(!(candidate <= ret && tmp < (root_sum - tmp)))
                dfs(root->right);
        }
    }
    int maxProduct(TreeNode* root) {
        ret = 0;
        root_sum = TreeSum(root);
        dfs(root);
        return ret % MOD;
    }
};
// @lc code=end

