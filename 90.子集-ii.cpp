/*
 * @lc app=leetcode.cn id=90 lang=cpp
 *
 * [90] 子集 II
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<algorithm>
#include<iostream>
using namespace std;

class SortedVectorSet{
public:
    int val;
    bool is_leaf;
    unordered_map<int, SortedVectorSet*> childs;
    SortedVectorSet():val(-1), is_leaf(false){}
    SortedVectorSet(int _val):val(_val), is_leaf(false){}
    bool count(const vector<int>& arr, int start = 0){
        if(arr.empty()) return is_leaf;
        if(start == arr.size() && is_leaf) return true;
        if(childs.count(arr[start]) == 0) return false;
        return childs[arr[start]]->count(arr, start + 1);
    }
    void insert(const vector<int>& arr, int start = 0){
        if(arr.empty()){is_leaf = true; return;}
        if(childs.count(arr[start]) == 0)childs[arr[start]] = new SortedVectorSet(arr[start]);
        if(start + 1 == arr.size()) childs[arr[start]]->is_leaf = true;
        else childs[arr[start]]->insert(arr, start + 1);
    }
};
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        SortedVectorSet s;
        vector<vector<int>> ret;
        int powered = 1 << nums.size();
        for(int i=0; i<powered; ++i){
            int tmp = i, idx = 0;
            vector<int> ttmp;
            while(tmp){
                if(tmp & 1)ttmp.push_back(nums[idx]);
                tmp >>= 1;
                ++idx;
            }
            if(s.count(ttmp)) continue;
            s.insert(ttmp);
            ret.push_back(ttmp);
        }
        return ret;
    }
};
// @lc code=end
int main(){
    vector<int> nums = {1, 2, 2};
    auto ret = Solution().subsetsWithDup(nums);
    for(auto & i: ret){
        for(auto j: i) cout << j << ' ';
        cout << '\n';
    }
    return 0;
}