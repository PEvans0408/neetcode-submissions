class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        frontindex = 0
        backindex = len(numbers) - 1
        while True:
            total = numbers[frontindex] + numbers[backindex]
            if total < target:
                frontindex += 1
            if total > target:
                backindex -= 1
            if total == target:
                return [frontindex + 1, backindex + 1]
            