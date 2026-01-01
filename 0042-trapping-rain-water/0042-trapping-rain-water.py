class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 # tracking height from left
        right = len(height) - 1 # tracking height from right
        left_max = height[0] # tracking max height seen from left
        right_max = height[-1] # tracking max height seen from right
        acc = 0 # tracking water total
        while left < right:
            # find which side is shorter and track that side as it is guaranteed to hold that much water from the other side
            if right_max < left_max:
                right -= 1 # go to next element find height that needs to be added to acc
                if height[right] < right_max: # if its smaller height than max seen so far, it can be safely added
                    acc += right_max - height[right]
                else: # otherwise no water gets added and max gets updated
                    right_max = height[right]
            # repeat same but for left side
            else:
                left += 1
                if height[left] < left_max:
                    acc += left_max - height[left]
                else:
                    left_max = height[left]
        return acc