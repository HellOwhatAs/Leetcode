/*
 * @lc app=leetcode.cn id=117 lang=cpp
 *
 * [117] 填充每个节点的下一个右侧节点指针 II
 */
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/
#include<iostream>
using namespace std;
class Solution {
public:
    Node* nextlevel(Node*root){
        if(root->left!=nullptr)return root->left;
        if(root->right!=nullptr)return root->right;
        if(root->next!=nullptr)return nextlevel(root->next);
        return nullptr;
    }
    Node* connect(Node* root) {
        if(root==nullptr)return root;
        connect(root->left);
        connect(root->right);
        for(auto a=root->left,b=root->right;a!=nullptr&&b!=nullptr;){
            auto tmp=a,_a=nextlevel(a),_b=nextlevel(b);
            while(tmp->next!=nullptr)tmp=tmp->next;
            tmp->next=b;
            a=_a;b=_b;
        }
        return root;
    }
};
// @lc code=end