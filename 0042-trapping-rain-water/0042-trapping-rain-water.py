class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        acc = 0
        while left < right:
            if right_max < left_max:
                right -= 1
                if height[right] < right_max:
                    acc += right_max - height[right]
                else:
                    right_max = height[right]
            else:
                left += 1
                if height[left] < left_max:
                    acc += left_max - height[left]
                else:
                    left_max = height[left]
        return acc