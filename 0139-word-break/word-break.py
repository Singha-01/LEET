class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        max_len = max((len(word) for word in wordDict), default=0)
        n = len(s)
        
        # dp[i] is True if s[0:i] can be segmented into words from wordDict
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            # Only look back up to max_len characters
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[n] 