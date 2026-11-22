from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_map = {}
        litter_count = 0
        start_r = start_c = 0
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
        
        target_mask = (1 << litter_count) - 1
        
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        if initial_mask == target_mask:
            return 0
        
        # Track max remaining energy seen for state (r, c, mask)
        # Using a 3D array for O(1) direct lookup instead of a hash dict
        max_energy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        
        queue = deque([(start_r, start_c, initial_mask, energy, 0)])
        max_energy[start_r][start_c][initial_mask] = energy
        
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()
            
            # If a faster route reached (r, c, mask) with strictly more energy, prune
            if cur_energy < max_energy[r][c][mask]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1
                    if next_energy < 0:
                        continue
                    
                    next_mask = mask
                    cell = classroom[nr][nc]
                    
                    if cell == 'R':
                        next_energy = energy
                    elif cell == 'L':
                        next_mask |= (1 << litter_map[(nr, nc)])
                    
                    if next_mask == target_mask:
                        return steps + 1
                    
                    # Strictly better energy pruning
                    if next_energy > max_energy[nr][nc][next_mask]:
                        max_energy[nr][nc][next_mask] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))
                        
        return -1