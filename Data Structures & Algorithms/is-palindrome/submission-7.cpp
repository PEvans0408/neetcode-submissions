class Solution {
public:
    bool isPalindrome(string s) {
        int frontindex = 0;
        int backindex = s.size() - 1;
        while (frontindex < backindex) {
            if (! isalnum(s[frontindex])) {
                frontindex++;
                continue;
            }
            if (! isalnum(s[backindex])) {
                backindex--;
                continue;
            }
            if (tolower(s[frontindex]) == tolower(s[backindex])) {
                frontindex++;
                backindex--;
            } else {
                return false;
            }
        }
        return true;
    }
};
