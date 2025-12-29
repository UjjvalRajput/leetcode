class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1
        while left_idx < right_idx:
            if numbers[left_idx] + numbers[right_idx] == target and left_idx != right_idx:
                return [left_idx + 1, right_idx + 1]
            else:
                if numbers[left_idx] + numbers[right_idx] > target:
                    right_idx -= 1
                else:
                    left_idx += 1