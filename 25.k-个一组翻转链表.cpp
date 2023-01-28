/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
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
    ListNode* reverse(ListNode*head,ListNode*last){
        ListNode *tmp=head,*tmp1=head->next,*tmp2;
        tmp->next=last;
        while(tmp1!=last){
            tmp2=tmp1->next;
            tmp1->next=tmp;
            tmp=tmp1;
            tmp1=tmp2;
        }
        return tmp;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1)return head;k--;
        bool f=1;
        ListNode* s=new ListNode,*e=head,*ret=s,*tmp;
        s->next=head;
        while(e!=nullptr){
            for(int i=0;i<k;++i){
                if(e->next==nullptr)return ret;
                e=e->next;
            }
            tmp=reverse(s->next,e->next);
            if(f){ret=tmp;f=0;}
            e=s->next;
            s->next=tmp;
            s=e;e=e->next;
        }
        return ret;
    }
};
// @lc code=end

