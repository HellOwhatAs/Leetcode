/*
 * @lc app=leetcode.cn id=1971 lang=cpp
 *
 * [1971] 寻找图中是否存在路径
 */

// @lc code=start
#include<vector>
using namespace std;
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
class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        bxjj a(n);
        for(auto&i:edges)a.hb(i.front(), i.back());
        return a.cha(source, destination);
    }
};
// @lc code=end

