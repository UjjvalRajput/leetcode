class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        acc = []
        for left in range(len(nums)-1): # index
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            middle = left + 1
            right = len(nums) - 1

            while middle < right:
                total = nums[left] + nums[middle] + nums[right]
                if total == 0:
                    acc.append([nums[left], nums[middle], nums[right]])
                    while middle < right and nums[middle] == nums[middle + 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    middle += 1
                    right -= 1
                elif total < 0:
                    middle += 1
                else:
                    right -= 1
        return acc