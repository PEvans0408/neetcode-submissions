class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.fibonacci(n, cache)
    
    def fibonacci(self, n: int, cache: dict):
        if n <= 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = self.fibonacci(n - 1, cache) + self.fibonacci(n - 2, cache)
        return cache[n]

            
