class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        str_nums = [str(num) for num in nums]
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0
        
        str_nums.sort(key=cmp_to_key(compare))
        if str_nums[0] == "0":
            return "0"
            
        return "".join(str_nums)