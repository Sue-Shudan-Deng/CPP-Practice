// https://leetcode.com/problems/contains-duplicate-iii

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k==0) {
            return false;
        }
        set<long long> s;
        for(int i=0; i<nums.size(); ++i){
            long long val = nums[i];
            if(!s.empty()){
                if (s.size()==k+1) {
                    s.erase(nums[i-k-1]);
                }
                auto higher = s.lower_bound(val);
                //higher points to smallest element bigger or equal to val
                if (higher!=s.end() && (*higher-val<=t)) {
                    return true;
                }
                if (higher != s.begin()) { 
                    higher--;
                    //now higher should point to biggest element smaller than val
                    auto low = higher;
                    if (low!=s.end() && ((val-*low)<=t))	{
                        return true;
                    }
                }
            }
            s.insert(val);
        }
        return false;
    }
};