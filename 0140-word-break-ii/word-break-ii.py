class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start: int) -> list[str]:
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursively solve for the remaining substring
                    for sub_sentence in backtrack(end):
                        if sub_sentence:
                            sentences.append(word + " " + sub_sentence)
                        else:
                            sentences.append(word)
                            
            memo[start] = sentences
            return sentences
            
        return backtrack(0)