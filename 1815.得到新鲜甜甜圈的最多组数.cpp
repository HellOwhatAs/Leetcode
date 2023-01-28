/*
 * @lc app=leetcode.cn id=1815 lang=cpp
 *
 * [1815] 得到新鲜甜甜圈的最多组数
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int maxHappyGroups(int batchSize, vector<int>& groups) {
        w = groups;
        n = w.size();
        m = batchSize;
        ans = 0;
        for(int i = 0; i < 80; i++) simulate_anneal();
        return ans;
    }

private:
    int n, m;
    vector<int> w;
    int ans;

    int calc() {
        int res = 1;
        for(int i = 0, s = 0; i < n; i++) {
            s = (s + w[i]) % m;
            if(!s && i < n - 1) res++;
        }
        ans = max(ans, res);
        return res;
    }

    void simulate_anneal() {
        random_shuffle(w.begin(), w.end());
        for(double t = 1e6; t > 1e-5; t *= 0.97) {
            int a = rand() % n, b = rand() % n;
            int x = calc();
            swap(w[a], w[b]);
            int y = calc();
            int delta = x - y;
            if(!(exp(-delta / t) > (double)rand() / RAND_MAX)) {
                swap(w[a], w[b]);
            }
        }
    }
};
// @lc code=end

