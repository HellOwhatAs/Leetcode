/*
 * @lc app=leetcode.cn id=128 lang=cpp
 *
 * [128] 最长连续序列
 */

// @lc code=start
#include<unordered_map>
using namespace std;
class bxjj{
public:
	int *data2,length;
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
    int longestConsecutive(vector<int>& nums) {
        bxjj a(nums.size());
        unordered_map<int,int> n2i;
        for(int i=0;i<nums.size();++i){
            if(n2i.count(nums[i]))continue;
            n2i[nums[i]]=i;
            if(n2i.count(nums[i]+1))a.hb(i,n2i[nums[i]+1]);
            if(n2i.count(nums[i]-1))a.hb(i,n2i[nums[i]-1]);
        }
        int ret=0;
        for(int i=0;i<a.length;++i){
            ret=min(ret,a.data2[i]);
        }
        return -ret;
    }
};
// @lc code=end

