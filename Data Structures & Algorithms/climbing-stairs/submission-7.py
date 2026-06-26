class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0: 1, 1: 1} #Avoid specifically recomputing base cases
        return self.fibonacci(n, cache)
    
    def fibonacci(self, n: int, cache: dict): #Idea is to cache previous fibonacci numbers to not have to recalculate needlessly
        if n <= 1:
            return 1
        if n in cache:
            return cache[n]
        print(f"Computing {n}")
        cache[n] = self.fibonacci(n - 1, cache) + self.fibonacci(n - 2, cache)
        return cache[n]

            
