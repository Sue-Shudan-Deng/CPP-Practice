// https://leetcode.com/problems/redundant-connection

class Solution {
private:
    int find(int node, vector<int>& parent) {
        while (node != parent[node]) {
            parent[node] = parent[parent[node]];
            node = parent[node];
        }
        return parent[node];
    }
    
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n + 1, 0);
        vector<int> size(n + 1, 0);
        
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (!parent[u]) {
                parent[u] = u;
            }
            if (!parent[v]) {
                parent[v] = v;
            }
            int pu = find(u, parent);
            int pv = find(v, parent);
            if (pu == pv) {
                return edge;
            }
            if (size[pu] < size[pv]) {
                swap(pu, pv);
            }
            parent[pv] = pu;
            size[pu] += size[pv];
        }
        return {};
    }
};