class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                i = num
                acc = 0
                while i in s:
                    acc += 1
                    i += 1
                longest = max(longest, acc)
        return longest
