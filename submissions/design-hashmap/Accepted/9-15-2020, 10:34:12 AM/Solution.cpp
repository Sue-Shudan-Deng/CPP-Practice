// https://leetcode.com/problems/design-hashmap

#define MAX_LEN 771
class MyHashMap {
    
private:
    vector<pair<int, int>> s[MAX_LEN];
    int getIndex(int key) {
        return key % MAX_LEN;
    }
    int getPos(int key, int idx) {
        for (int i = 0; i < s[idx].size(); ++i) {
            if (s[idx][i].first == key) {
                return i;
            }
        }
        return -1;
    }
    
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int idx = getIndex(key);
        int pos = getPos(key, idx);
        if (pos == -1) {
            s[idx].emplace_back(key, value);
        } else {
            s[idx][pos] = pair<int, int>{key, value};
        }
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int idx = getIndex(key);
        int pos = getPos(key, idx);
        if (pos == -1) {
            return pos;
        }
        return s[idx][pos].second;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int idx = getIndex(key);
        int pos = getPos(key, idx);
        if (pos >= 0) {
            s[idx].erase(s[idx].begin() + pos);
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */