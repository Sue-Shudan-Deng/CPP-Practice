// https://leetcode.com/problems/best-team-with-no-conflicts

class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        vector<pair<int, int>> a;
        int f[1010];
        int n;
        int i, j;
        n = scores.size();
        for (i = 0; i < n; ++i) a.push_back({ages[i], scores[i]});
        sort(a.begin(), a.end());
        int res = 0;
        for (i = 0; i < n; ++i){
            f[i] = a[i].second;
            for (j = 0; j < i; ++j){
                if (a[j].second > a[i].second) continue;
                f[i] = max(f[i], f[j] + a[i].second);
            }
            res = max(res, f[i]);
        }
        
        return res;
    }
};