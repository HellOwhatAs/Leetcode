/*
 * @lc app=leetcode.cn id=1669 lang=cpp
 *
 * [1669] 合并两个链表
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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *pa = list1, *pb = nullptr;
        for(int i = 1; i < a; ++i) pa = pa -> next;
        pb = pa;
        for(int i = a - 1; i <= b; ++i) pb = pb -> next;
        pa -> next = list2;
        while(pa -> next != nullptr) pa = pa -> next;
        pa -> next = pb;
        return list1;
    }
};
// @lc code=end

