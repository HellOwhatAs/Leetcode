/*
 * @lc app=leetcode.cn id=1147 lang=cpp
 *
 * [1147] 段式回文
 */

// @lc code=start
#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    bool reverse_eq(const string & a, const string & b){
        int n = a.size();
        if(n != b.size())return false;
        for(int i = 0; i < n; ++i)
            if(a[i] != b[n - 1 - i])return false;
        return true;
    }
    int longestDecomposition(string text) {
        int i = 0, j = text.size() - 1, count = 0;
        string left, right;
        while(i <= j){
            left.push_back(text[i]);
            right.push_back(text[j]);
            if(i == j)break;
            if(reverse_eq(left, right)){
                left.clear();
                right.clear();
                count += 2;
            }
            ++i;
            --j;
        }
        if(!left.empty() && !right.empty())++count;
        return count;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout << s.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi") << '\n'
         << s.longestDecomposition("merchant") << '\n'
         << s.longestDecomposition("antaprezatepzapreanta") << '\n';
    return 0;
}