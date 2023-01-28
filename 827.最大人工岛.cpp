/*
 * @lc app=leetcode.cn id=827 lang=cpp
 *
 * [827] 最大人工岛
 */

// @lc code=start
#include<vector>
#include<unordered_set>
#include<iostream>
#define Osearch(x,y) {if(grid[x][y]){tmp=bj.father(flatten({x,y}));if(!s.count(tmp))ret-=bj.data2[tmp];s.insert(tmp);}}
using namespace std;
class bxjj {
public:
	int* data2, length;
	int father(int x) {
		if (data2[x] < 0)return x;
		data2[x] = father(data2[x]);
		return data2[x];
	}
	bxjj(int l) {
		length = l;
		data2 = new int[length];
		for (int i = 0; i < length; i++)data2[i] = -1;
	}
	~bxjj() {
		delete[] data2;
	}
	void hb(int a, int b) {
		a = father(a);
		b = father(b);
		if (a == b)return;
		if (data2[a] < data2[b]) {
			data2[a] += data2[b];
			data2[b] = a;
		}
		else {
			data2[b] += data2[a];
			data2[a] = b;
		}
	}
	bool cha(int a, int b) {
		return father(a) == father(b);
	}
};
class Solution {
public:
    int n;
    unordered_set<int> s;
    int flatten(const pair<int,int>&x){
        return x.first*n+x.second;
    }
    int largestIsland(vector<vector<int>>& grid) {
        int ret=1,tmp,rret=1;
        n=grid.size();
        bxjj bj(n*n);
        for(int i=0;i<n;++i){
            for(int j=1;j<n;++j){
                if(grid[i][j-1]&&grid[i][j])bj.hb(flatten({i,j-1}),flatten({i,j}));
                if(grid[j-1][i]&&grid[j][i])bj.hb(flatten({j-1,i}),flatten({j,i}));
            }
        }
        bool flag=0;
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                if(grid[i][j]==0){
                    ret=1;
                    flag=1;
                    s.clear();
                    if(i>0)Osearch(i-1,j);
                    if(j>0)Osearch(i,j-1);
                    if(i<n-1)Osearch(i+1,j);
                    if(j<n-1)Osearch(i,j+1);
                    rret=max(rret,ret);
                }
            }
        }
        if(flag)return rret;
        rret=0;
        for(int i=0;i<bj.length;++i){
            rret=min(rret,bj.data2[i]);
        }
        return -rret;
    }
};
// @lc code=end

