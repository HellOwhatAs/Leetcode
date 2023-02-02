/*
 * @lc app=leetcode.cn id=872 lang=cpp
 *
 * [872] 叶子相似的树
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
using namespace std;
class Solution {
public:
    void getleaf(vector<int>& arr, TreeNode* root) {
        if(root -> left == nullptr && root -> right == nullptr) arr.push_back(root -> val);
        else if(root -> left == nullptr) getleaf(arr, root -> right);
        else if(root -> right == nullptr) getleaf(arr,  root -> left);
        else {
            getleaf(arr, root -> left);
            getleaf(arr, root ->right);
        }
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> a1, a2;
        getleaf(a1, root1);
        getleaf(a2, root2);
        return a1 == a2;
    }
};
// @lc code=end

