class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # to count max character appearance in window
        left = 0 # left pointer
        acc = 0 # results (substring with largest length)
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            acc = max(acc, right - left + 1)
        return acc