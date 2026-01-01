class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        acc = 0
        for i in range(len(nums) - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    acc += right - left
                    right -= 1
                else:
                    left += 1
        return acc