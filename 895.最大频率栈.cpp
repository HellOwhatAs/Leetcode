/*
 * @lc app=leetcode.cn id=895 lang=cpp
 *
 * [895] 最大频率栈
 */

// @lc code=start
#include<vector>
#include<unordered_map>
using namespace std;
class FreqStack {
    unordered_map<int,int> freq;
    unordered_map<int,vector<int>> stacks;
    int maxFreq;
public:
    FreqStack() {
        maxFreq=0;
        freq.clear();
        stacks.clear();
    }
    
    void push(int val) {
        stacks[++freq[val]].push_back(val);
        maxFreq=max(maxFreq,freq[val]);
    }
    
    int pop() {
        int ret=stacks[maxFreq].back();
        stacks[maxFreq].pop_back();
        --freq[ret];
        while(maxFreq && stacks[maxFreq].empty())--maxFreq;
        return ret;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
// @lc code=end

