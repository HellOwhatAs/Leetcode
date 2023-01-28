/*
 * @lc app=leetcode.cn id=99 lang=cpp
 *
 * [99] 恢复二叉搜索树
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
#include<vector>
using namespace std;
class Solution {
public:
    vector<TreeNode*> *arr;
    void midorder(TreeNode*root){
        if(root->left!=nullptr)midorder(root->left);
        arr->push_back(root);
        if(root->right!=nullptr)midorder(root->right);
    }
    void recoverTree(TreeNode* root) {
        vector<TreeNode*> v;
        arr=&v;
        midorder(root);
        if(v.size()==2)swap(v[0]->val,v[1]->val);
        else{
            vector<pair<int,int>> reversed;
            for(int i=1;i<v.size();++i)if(v[i-1]->val>v[i]->val)reversed.push_back({i-1,i});
            swap(v[reversed.front().first]->val,v[reversed.back().second]->val);
        }
    }
};
// @lc code=end

