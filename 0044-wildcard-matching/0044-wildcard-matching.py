class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        text_len = len(s)
        pattern_len = len(p)
        
        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (pattern_len + 1) for _ in range(text_len + 1)]
        
        # Empty text matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like "*", "**" that can match empty text
        for j in range(1, pattern_len + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                break
        
        # Fill the DP table
        for i in range(1, text_len + 1):
            for j in range(1, pattern_len + 1):
                if p[j - 1] == '*':
                    # '*' matches zero chars (dp[i][j-1]) or one/more chars (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' matches any single char, or exact character match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[text_len][pattern_len]
            