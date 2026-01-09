class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        ans = 0

        for right in range(len(nums)):
            # Fix duplicates
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Add current element
            seen.add(nums[right])
            curr_sum += nums[right]

            # Ensure window size <= k
            if right - left + 1 > k:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Record answer
            if right - left + 1 == k:
                ans = max(ans, curr_sum)

        return ans