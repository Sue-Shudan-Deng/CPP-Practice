// https://leetcode.com/problems/design-hashset

#define MAX_LEN 771
class MyHashSet {
    
private:
    vector<int> s[MAX_LEN];
    int getIndex(int key) {
        return key % MAX_LEN;
    }
    int getPos(int key, int idx) {
        auto itr = find(s[idx].begin(), s[idx].end(), key);
        if (itr == s[idx].end()) {
            return -1;
        }
        return itr - s[idx].begin();
    }
    
public:
    /** Initialize your data structure here. */
    MyHashSet() {}
    
    void add(int key) {
        int idx = getIndex(key);
        int pos = getPos(key, idx);
        if (pos == -1) {
            s[idx].push_back(key);
        }
    }
    
    void remove(int key) {
        int idx = getIndex(key);
        int pos = getPos(key, idx);
        if (pos >= 0) {
            s[idx].erase(s[idx].begin() + pos);
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int idx = getIndex(key);
        int pos = getPos(key, idx);
        bool ret = pos == -1 ? false : true;
        return ret;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */