class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for n in arr:
            if n in freq:
                freq[n] = freq[n] + 1
            else:
                freq[n] = 1
        counts = list(freq.values())

        return (len(counts) == len(set(counts)))
        