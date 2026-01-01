class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)): # left and right start at same place
            if nums[right] != 0: # find the next non-zero number (right) to replace with 0 (left)
                nums[left], nums[right] = nums[right], nums[left] # perform swap
                left += 1 # move left to next (potential) index with a 'zero' value