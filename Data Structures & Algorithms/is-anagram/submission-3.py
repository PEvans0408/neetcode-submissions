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
            else: usedCharacters[char] -= 1 #Do -= and not += with modular arithmetic to verify because that case breaks when you have s = 'xx' and t = 'bb' or smth like that
        
        for value in usedCharacters.values():
            if value == 0:
                continue
            else: return False
        return True


        