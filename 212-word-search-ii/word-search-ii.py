class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        WORD_KEY = "$"
        trie = {}
        
        # 1. Build the Trie from all target words
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[WORD_KEY] = word
            
        rows, cols = len(board), len(board[0])
        matched_words = []
        
        def backtrack(r: int, c: int, parent: dict) -> None:
            char = board[r][c]
            curr_node = parent[char]
            
            # 2. Check if we reached the end of a word
            word_match = curr_node.pop(WORD_KEY, None)
            if word_match:
                matched_words.append(word_match)
                
            # 3. Mark current cell as visited in-place
            board[r][c] = "#"
            
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    backtrack(nr, nc, curr_node)
                    
            # 4. Restore cell after exploring
            board[r][c] = char
            
            # 5. Optimization: Prune leaf nodes from the Trie once matched
            if not curr_node:
                parent.pop(char)
                
        # Trigger DFS from every cell that starts a word in the Trie
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    backtrack(r, c, trie)
                    
        return matched_words