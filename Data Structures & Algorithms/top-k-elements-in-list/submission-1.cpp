class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> groups;
        
        for (auto& num : nums) {
            groups[num]++;
        }
        
        vector<pair<int, int>> v(groups.begin(), groups.end());
        sort(v.begin(), v.end(), [](auto& a, auto& b) {
            return a.second > b.second;
        });
        //This uses a lambda function to sort by the magnitude of the value in the key-value pair.
        vector<int> retvect;
        for (int i = 0; i < k; i++) {
            retvect.push_back(v[i].first);
        } 
        //iterate over the first k values in this new sorted vector
        return retvect;
    }
};
