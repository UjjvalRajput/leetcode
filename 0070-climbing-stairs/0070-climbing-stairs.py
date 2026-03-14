class Solution:
    def climbStairs(self, n: int, seen=None) -> int:
        if seen is None:
            seen = {1:1, 2:2}

        if n in seen:
            return seen[n]

        seen[n] = self.climbStairs(n-1, seen) + self.climbStairs(n-2, seen)
        return seen[n]