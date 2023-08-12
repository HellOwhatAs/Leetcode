/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并 K 个升序链表
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lc code=start
#include<vector>
#include<queue>
#include<functional>
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b){
            if(a == nullptr) return true;
            if(b == nullptr) return false;
            return a->val > b->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(lists.begin(), lists.end(), cmp);
        ListNode* head = new ListNode;
        auto tail = head;
        while(!pq.empty() && pq.top() != nullptr){
            tail->next = pq.top();
            tail = tail->next;
            pq.pop();
            pq.push(tail->next);
        }
        tail->next = nullptr;
        return head->next;
    }
};
// @lc code=end

