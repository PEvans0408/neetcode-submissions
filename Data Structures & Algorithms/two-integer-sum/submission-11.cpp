class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int nums_size = nums.size();
        for (int i = 0; i < nums_size; i++) {
            int pointer1 = nums[i];
            for (int j = i + 1; j < nums_size; j++) {
                int pointer2 = nums[j];
                if (pointer1 + pointer2 == target) {
                    return {i, j};
                }   
            }
        }
    }
};
