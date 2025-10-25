class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        ans = 0
        for g in gain:
            curr += g
            if curr > ans:
                ans = curr
        return ans        

        