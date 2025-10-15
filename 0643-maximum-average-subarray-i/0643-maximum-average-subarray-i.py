class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        best_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            if curr_sum > best_sum:
                best_sum = curr_sum

        return best_sum / k

        