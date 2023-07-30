/*
 * @lc app=leetcode.cn id=142 lang=cpp
 *
 * [142] 环形链表 II
 */

#include<cstddef>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include<unordered_set>
using namespace std;
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> d;
        while(head != NULL){
            if(d.count(head)) return head;
            d.insert(head);
            head = head->next;
        }
        return NULL;
    }
};
// @lc code=end

