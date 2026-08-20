class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array of len [n] : rotated between 1 and n times
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]