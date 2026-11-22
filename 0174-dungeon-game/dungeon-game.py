class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # Initialize DP array with infinity; extra column handles right-boundary checks
        dp = [float('inf')] * (n + 1)
        
        # Base case: knight needs at least 1 HP right after rescuing the princess
        dp[n - 1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health_on_exit = min(dp[j], dp[j + 1])
                dp[j] = max(1, min_health_on_exit - dungeon[i][j])
                
        return dp[0]