class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = []
        for n in range(len(nums)): #n is the first index
            product = 1
            for m in range(len(nums)): #m is all indices != n
                if m != n:
                    product *= nums[m]
                else: continue
            output_array.append(product)
        return output_array