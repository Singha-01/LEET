class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtrack(start: int, path: list[int], remaining_sum: int):
            # Base case: exact length and sum reached
            if len(path) == k:
                if remaining_sum == 0:
                    res.append(path[:])
                return

            # Iterate through available digits 1 to 9
            for num in range(start, 10):
                # Pruning: since numbers increase, no further number can work
                if num > remaining_sum:
                    break
                
                path.append(num)
                backtrack(num + 1, path, remaining_sum - num)
                path.pop()  # Backtrack

        backtrack(1, [], n)
        return res