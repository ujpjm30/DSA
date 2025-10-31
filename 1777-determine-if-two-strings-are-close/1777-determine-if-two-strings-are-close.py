class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1 = Counter(word1)
        c2 = Counter(word2)

        if set(word1) == set(word2) and sorted(c1.values()) == sorted(c2.values()):
            return True
        return False

        