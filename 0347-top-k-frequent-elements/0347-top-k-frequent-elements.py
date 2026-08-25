class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        counts.most_common(k)
        result = [num for num, count in counts.most_common(k)]
        return result
        