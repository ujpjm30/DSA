class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            right = total - left -  x
            if left == right:
                return i
            left += x
        return -1