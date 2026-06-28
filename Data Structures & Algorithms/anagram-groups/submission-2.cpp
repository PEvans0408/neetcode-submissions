#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ret_vect;
        unordered_map<string, vector<string>> sorted_anagrams;
        for (string& str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            sorted_anagrams[key].push_back(str);
        }
        for (auto& pair : sorted_anagrams) {
            ret_vect.push_back(pair.second);
        }
        return ret_vect;
    }
};
