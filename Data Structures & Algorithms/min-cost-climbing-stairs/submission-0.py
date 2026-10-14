class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = cost[:2]

        while len(memo) < len(cost):
            i = len(memo)

            memo.append(cost[i]+ min(memo[i-1], memo[i-2]))

        return min(memo[-1], memo[-2]) 