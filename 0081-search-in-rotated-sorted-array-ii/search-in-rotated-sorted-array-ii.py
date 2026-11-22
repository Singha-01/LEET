class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates edge case
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Check if Left Half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, Right Half must be sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False