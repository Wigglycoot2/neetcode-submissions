class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1,2]

        if (n<=2):
            return memo[n-1]

        while len(memo) < n:
            memo.append(memo[len(memo)-1]+memo[len(memo)-2])

        return memo[-1]