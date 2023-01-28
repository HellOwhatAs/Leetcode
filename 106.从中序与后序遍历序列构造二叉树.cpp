/*
 * @lc app=leetcode.cn id=106 lang=cpp
 *
 * [106] 从中序与后序遍历序列构造二叉树
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
#include<unordered_map>
using namespace std;
class Solution {
public:
    vector<int> *in,*po;
    unordered_map<int,int> *val2ind;
    TreeNode* build(int ie,int pe,int l){
        if(l==0)return nullptr;
        int val=(*po)[pe], iind=(*val2ind)[val];
        TreeNode* ret=new TreeNode(val);
        ret->right=build(ie,pe-1,ie-iind);
        ret->left=build(iind-1,pe-(ie-iind+1),l-(ie-iind)-1);
        return ret;
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        in=&inorder;po=&postorder;
        val2ind=new unordered_map<int,int>;
        for(int i=0;i<inorder.size();++i)(*val2ind)[inorder[i]]=i;
        return build(inorder.size()-1,inorder.size()-1,inorder.size());
    }
};
// @lc code=end

