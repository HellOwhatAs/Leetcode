/*
 * @lc app=leetcode.cn id=864 lang=cpp
 *
 * [864] 获取所有钥匙的最短路径
 */

// @lc code=start
#include<vector>
#include<string>
#include<queue>
#include<tuple>
#include<iostream>
using namespace std;
class Solution {
public:
    int addkey(int x,char key){
        return x|(1<<(key-'a'));
    }
    bool haskey(int x,char lock){
        return x&(1<<(lock-'A'));
    }
    int shortestPathAllKeys(vector<string>& grid) {
        int m=grid.size(),n=grid.front().size(),start_i,start_j,tmp,keynum=0,distmp;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(grid[i][j]=='@'){
                    start_i=i;
                    start_j=j;
                }
                else if(grid[i][j]>='a'&&grid[i][j]<='f')++keynum;
            }
        }
        
        keynum=(1<<keynum)-1;
        queue<tuple<int,int,int>> q;
        q.push({start_i,start_j,0});
        vector<vector<vector<int>>> dis(m,vector<vector<int>>(n,vector<int>(64,INT_MAX)));
        dis[start_i][start_j][0]=0;

        while(!q.empty()){
            auto x=q.front();
            q.pop();
            tmp=grid[get<0>(x)][get<1>(x)];
            if(tmp>='a'&&tmp<='f'){
                distmp=dis[get<0>(x)][get<1>(x)][get<2>(x)];
                get<2>(x)=addkey(get<2>(x),tmp);
                dis[get<0>(x)][get<1>(x)][get<2>(x)]=distmp;
            }
            if(get<2>(x)==keynum)return dis[get<0>(x)][get<1>(x)][get<2>(x)];

            for(auto [_i,_j]:vector<pair<int,int>>{{1,0},{-1,0},{0,1},{0,-1}}){
                start_i=get<0>(x)+_i;
                start_j=get<1>(x)+_j;
                if( 
                    start_i>=0 && start_i<m &&
                    start_j>=0 && start_j<n &&
                    grid[start_i][start_j]!='#' &&
                    (
                        ( 
                            grid[start_i][start_j]>='A' && 
                            grid[start_i][start_j]<='F' && 
                            haskey(get<2>(x),grid[start_i][start_j]) 
                        ) ||
                        !(
                            grid[start_i][start_j]>='A' && 
                            grid[start_i][start_j]<='F'
                        )
                    ) && 
                    dis[start_i][start_j][get<2>(x)]==INT_MAX
                ){
                    q.push({start_i,start_j,get<2>(x)});
                    dis[start_i][start_j][get<2>(x)]=dis[get<0>(x)][get<1>(x)][get<2>(x)]+1;
                }
            }
        }
        return -1;
    }
};
// @lc code=end

