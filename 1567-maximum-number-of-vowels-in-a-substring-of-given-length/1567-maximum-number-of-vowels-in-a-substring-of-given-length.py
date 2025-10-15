class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        curr = sum(1 for ch in s[:k] if ch in vowels)
        best = curr

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1
            if curr > best:
                best = curr
                
        return best
        