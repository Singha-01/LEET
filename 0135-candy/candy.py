class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Pass 1: Left to Right
        # Satisfy left-neighbor condition
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Pass 2: Right to Left
        # Satisfy right-neighbor condition while keeping left condition valid
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)