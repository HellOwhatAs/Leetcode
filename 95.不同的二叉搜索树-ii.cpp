/*
 * @lc app=leetcode.cn id=95 lang=cpp
 *
 * [95] 不同的二叉搜索树 II
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
#include<iostream>
using namespace std;
class Solution {
public:
    vector<TreeNode*> func(int l,int r){
        if(l==r)return {nullptr};
        if(l+1==r)return {new TreeNode(l)};
        vector<TreeNode*> ret;
        for(int i=l;i<r;++i){
            for(auto p1:func(l,i)){
                for(auto p2:func(i+1,r)){
                    ret.push_back(new TreeNode(i,p1,p2));
                }
            }
        }
        return ret;
    }
    vector<TreeNode*> generateTrees(int n) {
        return func(1,n+1);
    }
};
// @lc code=end

