// https://leetcode.com/problems/similar-string-groups

class Solution {
    
private:
    map<string, string> parent;
    map<string, int> size;
    int cnt;
    string find(string x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void Union(string u, string v) {
        string pu = find(u);
        string pv = find(v);
        if (pu == pv) {
            // 当且仅当 union操作成功的时候,cnt才会-1
            return;
        }
        if (size[pu] < size[pv]) {
            swap(pu, pv);
        }
        parent[pv] = pu;
        size[pu] += size[pv];
        --cnt;
    }
    
    bool isSimilar(string s1, string s2) {
        int n = s1.size(), diff = 0;
        set<int> c1, c2;
        for (auto i = 0; i < n; ++i) {
            if (s1[i] != s2[i]) {
                ++diff;
                c1.insert(s1[i]);
                c2.insert(s2[i]);
            }
            if (diff > 2) {
                return false;
            }
        }
        return c1 == c2 ? true : false;
    }
    
public:
    int numSimilarGroups(vector<string>& A) {
        set<string> tmp(A.begin(), A.end());
        vector<string> new_A(tmp.begin(), tmp.end());
        for (auto s : new_A) {
            parent[s] = s;
            size[s] = 1;
        }
        cnt = new_A.size();
        int n = new_A.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isSimilar(new_A[i], new_A[j])) {
                    Union(new_A[i], new_A[j]);
                }
            }
        }
        return cnt;
    }
};