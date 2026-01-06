class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        acc = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])
            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            acc = max(acc, right - left + 1)
        return acc