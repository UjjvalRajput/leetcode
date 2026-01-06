class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # to count max character appearance in window
        left = 0 # left pointer
        acc = 0 # results (substring with largest length)
        for right in range(len(s)): # keep going right
            count[s[right]] = count.get(s[right], 0) + 1 # update count of encountered character
            if (right - left + 1) - max(count.values()) > k: # if window length - max char not to be changed = number of characters that are to be changed in the window is > no. of replacements allowed, the window becomes invalid. So, increment left to make window valid
                count[s[left]] -= 1 # decrement count of left as not including it anymore
                left += 1 # increment left pointer
            acc = max(acc, right - left + 1) # now calculate max results again after ensuring window is valid
        return acc # return max result