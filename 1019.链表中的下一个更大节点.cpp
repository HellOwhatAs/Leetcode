/*
 * @lc app=leetcode.cn id=1019 lang=cpp
 *
 * [1019] 链表中的下一个更大节点
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
#include <vector>
#include <stack>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        ListNode* p = head;
        stack<int*> s;
        while(p != nullptr){
            while(!s.empty() && *s.top() < p->val){
                *s.top() = p->val;
                s.pop();
            }
            s.push(&(p->val));
            p = p->next;
        }
        while(!s.empty()){
            *s.top() = 0;
            s.pop();
        }
        p = head;
        vector<int> ret;
        while(p != nullptr){
            ret.push_back(p->val);
            p = p->next;
        }
        return ret;
    }
};
// @lc code=end

int main() {
    Solution sol;
    ListNode* head = new ListNode(2, new ListNode(1, new ListNode(5)));
    auto ret = sol.nextLargerNodes(head);
    for(auto i:ret)cout<<i<<' ';
    return 0;
}