class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)

        if k >= n:
            return total
        
        left = 0
        curr = 0
        acc = 0
        
        for right in range(len(cardPoints)):
            curr += cardPoints[right]
            if right - left + 1 == n - k:
                acc = max(acc, total - curr)
                curr -= cardPoints[left]
                left += 1
        
        return acc