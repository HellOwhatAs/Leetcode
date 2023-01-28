/*
 * @lc app=leetcode.cn id=105 lang=cpp
 *
 * [105] 从前序与中序遍历序列构造二叉树
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
    unordered_map<int,int> *val2ind;
    vector<int> *pr,*in;
    TreeNode* build(int ps,int is,int l){
        if(l==0)return nullptr;
        TreeNode*ret=new TreeNode((*pr)[ps]);
        if(l==1)return ret;
        int iind=(*val2ind)[(*pr)[ps]];
        ret->left=build(ps+1,is,iind-is);
        ret->right=build(ps+1+iind-is,iind+1,is+l-iind-1);
        return ret;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        val2ind=new unordered_map<int,int>;
        for(int i=0;i<inorder.size();++i)(*val2ind)[inorder[i]]=i;
        pr=&preorder;in=&inorder;
        return build(0,0,inorder.size());
    }
};
// @lc code=end

