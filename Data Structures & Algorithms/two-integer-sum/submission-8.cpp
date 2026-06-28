class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap;
        for (int idx = 0; idx < nums.size(); idx++) {
            auto it = hashmap.find(target - nums[idx]);
            if (it != hashmap.end()) {
                vector<int> solution = {it->second, idx};
                return solution;
            }
            else {
                hashmap.emplace(nums[idx], idx);
            }   
        }
        return {};
    }
};
