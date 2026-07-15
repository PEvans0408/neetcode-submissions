class Solution:
    def isPalindrome(self, s: str) -> bool:
        frontindex = 0
        backindex = len(s) - 1
        while frontindex < backindex:    
            while frontindex < backindex and not s[frontindex].isalnum():
                frontindex += 1
            while frontindex < backindex and not s[backindex].isalnum():
                backindex -= 1
            if s[frontindex].lower() == s[backindex].lower():
                frontindex += 1
                backindex -= 1
            else: return False
        return True