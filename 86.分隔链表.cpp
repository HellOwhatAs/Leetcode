/*
 * @lc app=leetcode.cn id=86 lang=cpp
 *
 * [86] 分隔链表
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
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *p=new ListNode,*q=new ListNode,*tmp,*ret=p,*retq=q;
        q->next=nullptr;
        p->next=head;
        while(p->next!=nullptr){
            if(p->next->val<x)p=p->next;
            else{
                tmp=p->next->next;
                p->next->next=q->next;
                q->next=p->next;
                q=q->next;
                p->next=tmp;
            }
        }
        p->next=retq->next;
        delete retq;
        tmp=ret->next;
        delete ret;
        return tmp;
    }
};
// @lc code=end

