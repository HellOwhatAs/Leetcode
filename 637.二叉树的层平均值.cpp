/*
 * @lc app=leetcode.cn id=637 lang=cpp
 *
 * [637] 二叉树的层平均值
 */
#include<vector>
using namespace std;
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
    void count_node(TreeNode* root, int level, vector<double>& ret, vector<int>& ns) {
        if(root==nullptr)return;
        while(ret.size()<level+1){
            ret.push_back(0);
            ns.push_back(0);
        }
        ret[level]+=root->val;
        ns[level]++;
        count_node(root->left, level+1, ret, ns);
        count_node(root->right, level+1, ret, ns);
    }
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ret={0};
        vector<int> ns={0};
        count_node(root, 0, ret, ns);
        for(int i=0;i<ret.size();++i)ret[i]/=ns[i];
        return ret;
    }
};
// @lc code=end

