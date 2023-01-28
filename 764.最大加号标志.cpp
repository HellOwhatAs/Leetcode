/*
 * @lc app=leetcode.cn id=764 lang=cpp
 *
 * [764] 最大加号标志
 */

// @lc code=start
#include<vector>
#include<iostream>
#define print(left) {for(int i=0;i<n;++i){for(int j=0;j<n;++j){cout<<left[i][j]<<' ';}cout<<'\n';}cout<<"------\n";}
using namespace std;
class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        if(n==1||n*n==mines.size())return 0;
        int **left=new int*[n],**right=new int*[n],**up=new int*[n],**down=new int*[n];
        for(int i=0;i<n;++i){
            left[i]=new int[n];
            right[i]=new int[n];
            up[i]=new int[n];
            down[i]=new int[n];
            for(int j=0;j<n;++j){
                left[i][j]=up[i][j]=0;
                right[i][j]=down[i][j]=n;
            }
        }
        for(auto&k:mines){
            for(int i=k[1]+1;i<n;++i)if(left[k[0]][i]<k[1]+1)left[k[0]][i]=k[1]+1;
            for(int i=k[0]+1;i<n;++i)if(up[i][k[1]]<k[0]+1)up[i][k[1]]=k[0]+1;
            for(int i=0;i<k[1];++i)if(right[k[0]][i]>k[1])right[k[0]][i]=k[1];
            for(int i=0;i<k[0];++i)if(down[i][k[1]]>k[0])down[i][k[1]]=k[0];
        }
        for(auto&k:mines)left[k[0]][k[1]]=-1;
        int ret=0;
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                if(left[i][j]!=-1){
                    ret=max(ret,min(
                        min(j-left[i][j],right[i][j]-j-1),
                        min(i-up[i][j],down[i][j]-i-1)
                    ));
                }
            }
        }
        return ret+1;
    }
};
// @lc code=end

// 3\n[[0,2],[1,0],[2,0]]