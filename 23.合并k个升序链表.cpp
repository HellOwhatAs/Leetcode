/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并K个升序链表
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
#include<vector>
#include<queue>
using namespace std;
class Solution {
public:
    struct LNGreater{
        bool operator()(ListNode*a,ListNode*b){
            return a->val>b->val;
        }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        lists.erase(remove(lists.begin(), lists.end(), nullptr), lists.end());
        priority_queue<ListNode*,vector<ListNode*>,LNGreater> a(lists.begin(),lists.end());
        ListNode*ret=new ListNode,*tmp,*rret=ret;
        while(!a.empty()){
            ret->next=a.top();a.pop();
            ret=ret->next;
            if(ret->next!=nullptr)a.push(ret->next);
        }
        return rret->next;
    }
};
// @lc code=end

