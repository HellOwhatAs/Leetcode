/*
 * @lc app=leetcode.cn id=707 lang=cpp
 *
 * [707] 设计链表
 */

// @lc code=start
class MyLinkedList {
    struct node{
        int val;
        node*next;
        node(int v):val(v),next(nullptr){}
        node(int v,node* _next):val(v),next(_next){}
    };
    node* head,*tmp;
public:
    MyLinkedList() {
        head=new node(0);
    }
    ~MyLinkedList() {
        tmp=head;
        node* _;
        while(tmp!=nullptr){
            _=tmp->next;
            delete tmp;
            tmp=_;
        }
    }
    int get(int index) {
        if(index<0||index>=head->val)return -1;
        tmp=head;
        for(;index>=0;--index)tmp=tmp->next;
        return tmp->val;
    }
    
    void addAtHead(int val) {
        head->next=new node(val,head->next);
        ++head->val;
    }
    
    void addAtTail(int val) {
        tmp=head;
        for(int i=0;i<head->val;++i)tmp=tmp->next;
        tmp->next=new node(val,tmp->next);
        ++head->val;
    }
    
    void addAtIndex(int index, int val) {
        if(index==head->val)addAtTail(val);
        else if(index>head->val)return;
        else if(index<0)addAtHead(val);
        else{
            tmp=head;
            for(;index>0;--index)tmp=tmp->next;
            tmp->next=new node(val,tmp->next);
            ++head->val;
        }
    }
    
    void deleteAtIndex(int index) {
        if(index<0||index>=head->val)return;
        tmp=head;
        for(;index>0;--index)tmp=tmp->next;
        auto _=tmp->next;
        tmp->next=tmp->next->next;
        --head->val;
        delete _;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
// @lc code=end

