/*
 * @lc app=leetcode.cn id=92 lang=cpp
 *
 * [92] 反转链表 II
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int count=1;
        ListNode* p=new ListNode,*ret=p,*q=nullptr,*retq,*tmp;
        p->next=head;
        while(count<left){
            p=p->next;
            ++count;
        }
        while(count<=right){
            tmp=p->next->next;
            p->next->next=q;
            if(q==nullptr)retq=p->next;
            q=p->next;
            p->next=tmp;
            ++count;
        }
        retq->next=p->next;
        p->next=q;
        tmp=ret->next;
        delete ret;
        return tmp;
    }
};
// @lc code=end

