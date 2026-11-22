class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the slope goes down, a peak must exist on the left (including mid)
            if nums[mid] > nums[mid + 1]:
                right = mid
            # If the slope goes up, a peak must exist on the right
            else:
                left = mid + 1
                
        return left