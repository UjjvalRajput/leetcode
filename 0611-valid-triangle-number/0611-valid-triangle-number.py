class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        acc = 0
        for i in range(len(nums) - 1, 1, -1): # ignore the first two values as i because those will be for l and r
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    acc += right - left # add all values between l and r
                    right -= 1 # try with a different r
                else:
                    left += 1 # smallest value is too small try a bigger value instead.
        return acc