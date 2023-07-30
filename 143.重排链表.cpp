/*
 * @lc app=leetcode.cn id=143 lang=cpp
 *
 * [143] 重排链表
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// @lc code=start
#include<queue>
using namespace std;
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
    void reorderList(ListNode* head) {
        deque<ListNode*> q;
        while (head != nullptr) {
            q.push_back(head);
            head = head->next;
        }
        while (true) {
            if(q.empty()) break;
            q.front()->next = (q.size() <= 1)? nullptr: q.back();
            q.pop_front();
            if(q.empty()) break;
            q.back()->next = (q.size() <= 1)? nullptr: q.front();
            q.pop_back();
        }
    }
};
// @lc code=end
