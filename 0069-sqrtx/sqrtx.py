class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid <= x:
                ans = mid        # mid is a valid integer square root, try finding a larger one
                left = mid + 1
            else:
                right = mid - 1  # mid^2 is too big, search in lower half
                
        return ans