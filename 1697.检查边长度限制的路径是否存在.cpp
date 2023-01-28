/*
 * @lc app=leetcode.cn id=1697 lang=cpp
 *
 * [1697] 检查边长度限制的路径是否存在
 */

// @lc code=start
#include<vector>
#include<algorithm>
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
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        bxjj a(n);
        vector<int> order;
        vector<bool> ret(queries.size());
        sort(edgeList.begin(), edgeList.end(), [](const vector<int>& a, const vector<int>& b){return a.back()<b.back();});
        for(int i=0;i<queries.size();++i)order.push_back(i);
        sort(order.begin(), order.end(), [&queries](int a, int b){return queries[a].back()<queries[b].back();});
        int edge_idx=0;
        for(auto i:order){
            while(edge_idx<edgeList.size() && edgeList[edge_idx].back()<queries[i].back()){
                a.hb(edgeList[edge_idx][0], edgeList[edge_idx][1]);
                ++edge_idx;
            }
            ret[i]=a.cha(queries[i][0], queries[i][1]);
        }
        return ret;
    }
};
// @lc code=end
// 5\n[[0,1,10],[1,2,5],[2,3,9],[3,4,13]]\n[[0,4,14],[1,4,13]]
