/*
 * @lc app=leetcode.cn id=108 lang=cpp
 *
 * [108] 将有序数组转换为二叉搜索树
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
    vector<int> *arr;
    TreeNode* buildtree(int l, int r){
        if(l==r)return nullptr;
        if(r==l+1)return new TreeNode((*arr)[l]);
        int mid=(l+r)/2;
        return new TreeNode((*arr)[mid],buildtree(l,mid),buildtree(mid+1,r));
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        arr=&nums;
        return buildtree(0,nums.size());
    }
};
// @lc code=end

