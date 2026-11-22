class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # 'k' tracks the position for the next valid element
        k = 2
        
        for i in range(2, len(nums)):
            # If current element is different from the element 2 positions back in the valid portion
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k
        