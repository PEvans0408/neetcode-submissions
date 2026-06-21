class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        usedCharacters = {}
        for char in s:
            if char not in usedCharacters.keys():
                usedCharacters[f'{char}'] = 1
            else: usedCharacters[char] += 1
        for char in t:
            if char not in usedCharacters.keys():
                usedCharacters[f'{char}'] = 1
            else: usedCharacters[char] -= 1
        
        for value in usedCharacters.values():
            if value == 0:
                continue
            else: return False
        return True


        