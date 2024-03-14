class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1] Find right = the smallest number
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[right]