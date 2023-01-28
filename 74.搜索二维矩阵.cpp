/*
 * @lc app=leetcode.cn id=74 lang=cpp
 *
 * [74] 搜索二维矩阵
 */

// @lc code=start
#include<algorithm>
#include<vector>
using namespace std;
class Solution {
public:
    struct mycmp{
        int m,n,t;
        vector<vector<int>> *ddata;
        mycmp(int _m,int _n,int _t,vector<vector<int>> *_ddata):m(_m),n(_n),t(_t),ddata(_ddata){}
        bool operator()(int a,int b){
            return ((a==-1)?t:(*ddata)[a/n][a%n])<((b==-1)?t:(*ddata)[b/n][b%n]);
        }
    };
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size(),n=matrix[0].size();
        int *a=new int[m*n];
        for(int i=0;i<m*n;++i)a[i]=i;
        return binary_search(&a[0],&a[m*n],-1,mycmp(m,n,target,&matrix));
    }
};
// @lc code=end