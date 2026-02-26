class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        best = 0
        zeros = deque()  

        for right, x in enumerate(nums):
            if x == 0:
                zeros.append(right)

            if len(zeros) > k:
                left = zeros.popleft() + 1

            best = max(best, right - left + 1)

        return best
        