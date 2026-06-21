class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            pointer1 = nums[n]
            for m in range(len(nums)):
                if m != n:
                    pointer2 = nums[m]
                    if pointer1 + pointer2 == target:
                        return [n, m]
                continue
        return []