/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *ret=new ListNode,*tmp=new ListNode;
        tmp->next=ret;
        int s=0, now_val;
        while(l1!=nullptr&&l2!=nullptr){
            tmp=tmp->next;
            now_val=l1->val+l2->val+s;
            tmp->val=now_val%10;
            s=now_val/10;
            l1=l1->next;
            l2=l2->next;
            tmp->next=new ListNode;
        }
        while(l1!=nullptr){
            tmp=tmp->next;
            now_val=l1->val+s;
            tmp->val=now_val%10;
            s=now_val/10;
            if(s==0){
                tmp->next=l1->next;
                return ret;
            }
            tmp->next=new ListNode;
            l1=l1->next;
        }
        while(l2!=nullptr){
            tmp=tmp->next;
            now_val=l2->val+s;
            tmp->val=now_val%10;
            s=now_val/10;
            if(s==0){
                tmp->next=l2->next;
                return ret;
            }
            tmp->next=new ListNode;
            l2=l2->next;
        }
        if(s)tmp->next->val=s;
        else tmp->next=nullptr;
        return ret;
    }
};
// @lc code=end

