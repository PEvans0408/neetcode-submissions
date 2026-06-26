class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        
        def minCost(i):
            if i >= len(cost):
                return 0
            elif i in cache:
                return cache[i]
            else: 
                cache[i] = cost[i] + min(minCost(i + 1), minCost(i + 2))
                return cache[i]
        
        return min(minCost(0), minCost(1))


        
        
