/*
 * @lc app=leetcode.cn id=1356 lang=cpp
 *
 * [1356] 根据数字二进制下 1 的数目排序
 */

// @lc code=start
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    struct {
        int bits(int x) {
            int ret = 0;
            while(x) {
                ret += x & 1;
                x >>= 1;
            }
            return ret;
        }
        bool operator()(int a, int b) {
            int ba = bits(a), bb = bits(b);
            if(ba == bb) return a < b;
            return ba < bb;
        }
    } BitsComp;
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), BitsComp);
        return arr;
    }
};
// @lc code=end

