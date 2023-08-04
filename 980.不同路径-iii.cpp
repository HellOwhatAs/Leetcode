/*
 * @lc app=leetcode.cn id=980 lang=cpp
 *
 * [980] 不同路径 III
 */

// @lc code=start
#include<vector>
#include<tuple>
#include<unordered_map>

#ifdef _MSC_VER
#  include <intrin.h>
#  define __builtin_popcount __popcnt
#endif


#include <tuple>
namespace std{
    namespace
    {

        // Code from boost
        // Reciprocal of the golden ratio helps spread entropy
        //     and handles duplicates.
        // See Mike Seymour in magic-numbers-in-boosthash-combine:
        //     http://stackoverflow.com/questions/4948780

        template <class T>
        inline void hash_combine(std::size_t& seed, T const& v)
        {
            seed ^= std::hash<T>()(v) + 0x9e3779b9 + (seed<<6) + (seed>>2);
        }

        // Recursive template code derived from Matthieu M.
        template <class Tuple, size_t Index = std::tuple_size<Tuple>::value - 1>
        struct HashValueImpl
        {
          static void apply(size_t& seed, Tuple const& tuple)
          {
            HashValueImpl<Tuple, Index-1>::apply(seed, tuple);
            hash_combine(seed, std::get<Index>(tuple));
          }
        };

        template <class Tuple>
        struct HashValueImpl<Tuple,0>
        {
          static void apply(size_t& seed, Tuple const& tuple)
          {
            hash_combine(seed, std::get<0>(tuple));
          }
        };
    }

    template <typename ... TT>
    struct hash<std::tuple<TT...>> 
    {
        size_t
        operator()(std::tuple<TT...> const& tt) const
        {                                              
            size_t seed = 0;                             
            HashValueImpl<std::tuple<TT...> >::apply(seed, tt);    
            return seed;                                 
        }                                              

    };
}



using namespace std;
class Solution {
public:
    vector<vector<int>> self_grid;
    int m, n, length;
    unordered_map<tuple<int, int, int>, int> cache;

    int grid_count(int val){
        int ret = 0;
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                ret += (self_grid[i][j] == val);
            }
        }
        return ret;
    }

    pair<int, int> grid_search(int val){
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                if(self_grid[i][j] == val) return {i, j};
            }
        }
        return {-1, -1};
    }

    void set_state(int i, int j, int& state){
        state |= (1 << (i * n + j));
    }

    int get_state(int i, int j, int state){
        return (state >> (i * n + j)) & 1;
    }

    int dfs(int i, int j, int state){
        auto key = make_tuple(i, j, state);
        if(cache.count(key)) return cache[key];

        if(self_grid[i][j] == 2) return cache[key] = (__builtin_popcount(state) == length);
        set_state(i, j, state);
        int ret = 0;
        for(auto&[di, dj]: vector<pair<int, int>>({{-1, 0}, {0, -1}, {1, 0}, {0, 1}})){
            int i1 = i + di, j1 = j + dj;
            if (i1 < 0 || i1 >= m 
                || j1 < 0 || j1 >= n
                || self_grid[i1][j1] == -1
                || get_state(i1, j1, state)) continue;
            ret += dfs(i1, j1, state);
        }
        return cache[key] = ret;
    }

    int uniquePathsIII(vector<vector<int>>& grid) {
        cache.clear();
        self_grid.swap(grid);
        m = self_grid.size(), n = self_grid.front().size();
        length = grid_count(0) + 1;
        auto [i, j] = grid_search(1);
        return dfs(i, j, 0);
    }
};
// @lc code=end

