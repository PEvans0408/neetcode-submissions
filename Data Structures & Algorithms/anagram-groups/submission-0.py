class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        usedCharacters = {}
        for char in s:
            if char not in usedCharacters.keys():
                usedCharacters[f'{char}'] = 1
            else: 
                usedCharacters[char] += 1
        for char in t:
            if char not in usedCharacters.keys():
                return False  # If char not in s, it's not an anagram
            else: 
                usedCharacters[char] -= 1
        for value in usedCharacters.values():
            if value != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramSublists = []
        remaining = strs.copy()  # Keep track of unprocessed strings
        
        while remaining:  # Keep going until all strings are grouped
            current = remaining[0]  # Take first remaining string
            current_group = [current]  # Start a new group with this string
            to_remove = [0]  # Track indices to remove (starting with index 0)
            
            # Check all other remaining strings
            for i in range(1, len(remaining)):
                if self.isAnagram(current, remaining[i]):
                    current_group.append(remaining[i])
                    to_remove.append(i)
            
            # Remove all anagrams (in reverse order to avoid index shifting)
            for idx in sorted(to_remove, reverse=True):
                remaining.pop(idx)
            
            anagramSublists.append(current_group)
        
        return anagramSublists