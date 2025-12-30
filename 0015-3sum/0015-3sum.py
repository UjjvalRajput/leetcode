class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for left in range(n - 2):
            # skip duplicate fixed values
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            middle = left + 1
            right = n - 1

            while middle < right:
                s = nums[left] + nums[middle] + nums[right]

                if s == 0:
                    res.append([nums[left], nums[middle], nums[right]])

                    # skip duplicates for middle
                    while middle < right and nums[middle] == nums[middle + 1]:
                        middle += 1
                    # skip duplicates for right
                    while middle < right and nums[right] == nums[right - 1]:
                        right -= 1

                    middle += 1
                    right -= 1

                elif s < 0:
                    middle += 1
                else:
                    right -= 1

        return res