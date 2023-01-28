/*
 * @lc app=leetcode.cn id=88 lang=cpp
 *
 * [88] 合并两个有序数组
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> tmp(nums1.begin(),nums1.begin()+m);
        int i1=0,i2=0;
        while(i1<m&&i2<n){
            if(tmp[i1]<nums2[i2]){
                nums1[i1+i2]=tmp[i1];
                ++i1;
            }
            else {
                nums1[i1+i2]=nums2[i2];
                ++i2;
            }
        }
        while(i1<m){
            nums1[i1+i2]=tmp[i1];
            ++i1;
        }
        while(i2<n){
            nums1[i1+i2]=nums2[i2];
            ++i2;
        }
    }
};
// @lc code=end

