class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        top = counts.most_common(k)
        result = []
        for num, count in top:
            result.append(num)
        return result
        