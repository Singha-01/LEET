from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            
            # Only check j > i since lines through earlier points were already counted
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dy = y2 - y1
                dx = x2 - x1
                
                if dx == 0:
                    slope = (1, 0)  # Vertical line
                elif dy == 0:
                    slope = (0, 1)  # Horizontal line
                else:
                    # Normalize sign so dx is always positive
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    g = gcd(abs(dy), dx)
                    slope = (dy // g, dx // g)
                
                slopes[slope] += 1
                max_points = max(max_points, slopes[slope] + 1)
                
        return max_points