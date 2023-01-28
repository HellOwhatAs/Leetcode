/*
 * @lc app=leetcode.cn id=705 lang=cpp
 *
 * [705] 设计哈希集合
 */

// @lc code=start
class MyHashSet {
public:
    bool *arr;
    MyHashSet() {
        arr=new bool[1000001]();
    }
    ~MyHashSet() {
        delete [] arr;
    }
    void add(int key) {
        arr[key]=1;
    }
    
    void remove(int key) {
        arr[key]=0;
    }
    
    bool contains(int key) {
        return arr[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
// @lc code=end

