class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int frontindex = 0;
        int backindex = numbers.size() - 1;
        while (true) {
            int sum = numbers[frontindex] + numbers[backindex];
            if (sum == target) {
                return vector<int>{frontindex + 1, backindex + 1};
            }
            if (sum > target) {
                backindex--;
            } else frontindex++;
            
        }
    }
};
