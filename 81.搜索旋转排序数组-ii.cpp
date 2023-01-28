/*
 * @lc app=leetcode.cn id=81 lang=cpp
 *
 * [81] 搜索旋转排序数组 II
 */

// @lc code=start
#include<algorithm>
#include<vector>
using namespace std;
class Solution {
public:
    struct mycmp{
        int l,r;
        mycmp(int _l,int _r):l(_l),r(_r){}
        bool operator()(int b,int a){
            return (l<=r||a>=l&&b>=l||a<=r&&b<=r)?a>b:(a<l||b>r);
        }
    };
    bool search(vector<int>& nums, int target) {
        if(nums.front()==target)return true;
        while(!nums.empty()&&nums.back()==nums.front())nums.pop_back();
        if(nums.empty())return false;
        int l=nums[0],r=nums[nums.size()-1];
        auto ind=lower_bound(nums.begin(),nums.end(),target,mycmp(l,r));
        if(ind==nums.end()||*ind!=target)return false;
        return true;
    }
};
// @lc code=end

