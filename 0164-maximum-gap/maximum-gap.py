class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        # Calculate minimum possible maximum gap (bucket width)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Store [min, max] for each bucket
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Place each number into its corresponding bucket
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
            
        # Scan buckets to find the largest gap between adjacent non-empty buckets
        max_gap = 0
        prev_max = min_val
        
        for b_min, b_max in buckets:
            if b_min == float('inf'):  # Skip empty buckets
                continue
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max
            
        return max_gap