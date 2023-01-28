/*
 * @lc app=leetcode.cn id=113 lang=cpp
 *
 * [113] 路径总和 II
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
#include<numeric>
using namespace std;
class Solution {
public:
    vector<vector<int>> ret;
    int tar;
    void dfs(TreeNode* root,vector<int>&path){
        path.push_back(root->val);
        if(root->left==nullptr&&root->right==nullptr){
            if(accumulate(path.begin(),path.end(),0)==tar)ret.emplace_back(path);
        }
        else{
            if(root->left!=nullptr)dfs(root->left,path);
            if(root->right!=nullptr)dfs(root->right,path);
        }
        path.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if(root==nullptr)return {};
        ret.clear();
        tar=targetSum;
        vector<int> tmp;
        dfs(root,tmp);
        return ret;
    }
};
// @lc code=end

