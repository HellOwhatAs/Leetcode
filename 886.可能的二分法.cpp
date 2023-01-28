/*
 * @lc app=leetcode.cn id=886 lang=cpp
 *
 * [886] 可能的二分法
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
#ifdef bxjj
class Solution {
public:
    struct node{
        int val, color;
        vector<node*> links;
    };
    node* ns;
    bool dfs(node* x){
        for(auto i:x->links){
            if(i->color==x->color)return false;
            else if(i->color==-1){
                i->color=!x->color;
                if(!dfs(i))return false;
            }
        }
        return true;
    }
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        ns=new node[n];
        for(int i=0;i<n;++i){
            ns[i].val=i;
            ns[i].color=-1;
        }
        for(auto&i:dislikes){
            ns[i[0]-1].links.push_back(&ns[i[1]-1]);
            ns[i[1]-1].links.push_back(&ns[i[0]-1]);
        }
        for(int i=0;i<n;++i){
            if(ns[i].color==-1){
                ns[i].color=0;
                if(!dfs(&ns[i])){
                    delete [] ns;
                    return false;
                }
            }
        }
        delete [] ns;
        return true;
    }
};
#else
class Solution {
public:
    class bxjj{
    private:
        int *data2,length;
    public:
        int father(int x){
            if(data2[x]<0)return x;
            data2[x]=father(data2[x]);
            return data2[x];
        }
        bxjj(int l){
            length=l;
            data2=new int[length];
            for(int i=0;i<length;i++)data2[i]=-1;
        }
        ~bxjj(){
            delete [] data2;
        }
        void hb(int a,int b){
            a=father(a);
            b=father(b);
            if(a==b)return;
            if(data2[a]<data2[b]){
                data2[a]+=data2[b];
                data2[b]=a;
            }
            else {
                data2[b]+=data2[a];
                data2[a]=b;
            }
        }
        bool cha(int a,int b){
            return father(a)==father(b);
        }
    };
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        bxjj a(n);
        vector<vector<int>> dis(n);
        for(auto&i:dislikes){
            dis[i[0]-1].push_back(i[1]-1);
            dis[i[1]-1].push_back(i[0]-1);
        }
        for(int i=0;i<n;++i){
            for(auto j:dis[i]){
                a.hb(dis[i][0],j);
                if(a.cha(i,j))return false;
            }
        }
        return true;
    }
};
#endif
// @lc code=end




