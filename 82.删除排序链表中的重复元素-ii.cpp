/*
 * @lc app=leetcode.cn id=82 lang=cpp
 *
 * [82] 删除排序链表中的重复元素 II
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p=new ListNode,*ret=p;
        while(head!=nullptr){
            p->next=head;head=head->next;
            if(head==nullptr){p->next->next=nullptr;return ret->next;}
            if(p->next->val==head->val){
                head=head->next;
                while(head!=nullptr&&p->next->val==head->val)head=head->next;
            }
            else p=p->next;
        }
        p->next=nullptr;
        return ret->next;
    }
};
// @lc code=end

