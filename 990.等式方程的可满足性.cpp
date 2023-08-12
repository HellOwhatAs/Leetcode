/*
 * @lc app=leetcode.cn id=990 lang=cpp
 *
 * [990] 等式方程的可满足性
 */

// @lc code=start
#include<vector>
#include<string>
#include<unordered_map>
using namespace std;

class DisjointSet{
public:
    int size;
    vector<int> data;
    DisjointSet(int _size): size(_size), data(_size, -1) {}
    int query(int val){
        if(data[val] < 0) return val;
        return data[val] = query(data[val]);
    }
    void merge(int a, int b){
        int root_a = query(a), root_b = query(b);
        if(root_a == root_b) return;
        if(data[root_a] > data[root_b]) swap(root_a, root_b);
        auto tmp = data[root_b];
        data[root_b] = root_a;
        data[root_a] += tmp;
    }
};

class Solution {
public:
    bool equationsPossible(const vector<string>& equations) {
        unordered_map<char, int> char2idx;
        for(auto& eq: equations){
            if(!char2idx.count(eq.front())) char2idx[eq.front()] = char2idx.size();
            if(!char2idx.count(eq.back())) char2idx[eq.back()] = char2idx.size();
        }
        DisjointSet djs(char2idx.size());
        for(auto& eq: equations){
            if(eq[1] == '=') djs.merge(char2idx[eq.front()], char2idx[eq.back()]);
        }
        for(auto& eq: equations){
            if(eq[1] == '!' && djs.query(char2idx[eq.front()]) == djs.query(char2idx[eq.back()])) return false;
        }
        return true;
    }
};
// @lc code=end

#include<iostream>
int main(){
    cout << Solution().equationsPossible({"a==b", "b!=a"}) << '\n'
         << Solution().equationsPossible({"b==a", "a==b"}) << '\n'
         << Solution().equationsPossible({"a==b", "b==c", "a==c"}) << '\n'
         << Solution().equationsPossible({"a==b", "b!=c", "c==a"}) << '\n'
         << Solution().equationsPossible({"c==c", "b==d", "x!=z"}) << '\n';
    return 0;
}