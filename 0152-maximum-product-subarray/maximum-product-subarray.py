class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1
        
        for n in nums:
            # Save cur_max * n before updating cur_max
            temp_max = cur_max * n
            cur_max = max(n, temp_max, cur_min * n)
            cur_min = min(n, temp_max, cur_min * n)
            
            res = max(res, cur_max)
            
        return res