class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = Counter(words)
        pairs = []
        for word in counts:
            pairs.append((-counts[word], word))

        pairs = sorted(pairs)

        result = []
        for pair in pairs[:k]:
            result.append(pair[1])
        return result
        