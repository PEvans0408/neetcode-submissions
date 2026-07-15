class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for pointer1 in range(len(numbers)):    
            for pointer2 in range(len(numbers)):
                if numbers[pointer1] != numbers[pointer2]:
                    if numbers[pointer1] + numbers[pointer2] == target:
                        return [pointer1 + 1, pointer2 + 1]
