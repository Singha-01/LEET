class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            # Update 'ones' with bits that are not in 'twos'
            ones = (ones ^ num) & ~twos
            # Update 'twos' with bits that are not in 'ones'
            twos = (twos ^ num) & ~ones
            
        return ones