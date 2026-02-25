class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        for c in candies:
            result.append(c + extraCandies >= max_candy)
        return result
        