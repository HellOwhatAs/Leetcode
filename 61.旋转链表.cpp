/*
 * @lc app=leetcode.cn id=61 lang=cpp
 *
 * [61] 旋转链表
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include<iostream>
using namespace std;
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==nullptr||k==0)return head;
        int l=0;
        for(auto i=head;i!=nullptr;i=i->next,++l);
        k%=l;
        if(k==0)return head;
        ListNode* ret=head,*tail;
        for(int i=1;i<l-k;++i)ret=ret->next;
        tail=ret;
        ret=ret->next;
        tail->next=nullptr;
        tail=ret;
        for(int i=1;i<k;++i)tail=tail->next;
        tail->next=head;
        return ret;
    }
};
// @lc code=end

