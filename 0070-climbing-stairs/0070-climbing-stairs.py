class Solution:
    def climbStairs(self, n: int) -> int:
        # for recursion - memoization, we can add another parameter seen to the function above:
        # if seen is None:
        #     seen = {1:1, 2:2}
        # if n <= 2:
        #     return n

        # elif n in seen:
        #     return seen[n]

        # seen[n] = self.climbStairs(n-1, seen) + self.climbStairs(n-2, seen)
        # return seen[n]
        if n <= 2:
            return n
        
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]