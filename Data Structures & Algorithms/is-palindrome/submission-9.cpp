class Solution {
public:
    bool isPalindrome(string s) {
        int frontindex = 0;
        int backindex = s.size() - 1;
        while (frontindex < backindex) {
            while (frontindex < backindex && ! isalnum(s[frontindex])) {
                frontindex++;
            }
            while (frontindex < backindex && ! isalnum(s[backindex])) {
                backindex--;
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
