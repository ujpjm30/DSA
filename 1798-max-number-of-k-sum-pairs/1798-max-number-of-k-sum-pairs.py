class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ops = 0
        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                ops += 1
                i += 1
                j -= 1
            elif s < k:
                i += 1
            else:
                j -= 1

        return ops    
        