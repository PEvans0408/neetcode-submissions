class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        for num in nums:
            key = str(num)
            if key not in groups:
                groups[f'{num}'] = 1
            else: groups[f'{num}'] += 1
        
        return sorted(groups, key=groups.get, reverse=True)[:k]
        
            