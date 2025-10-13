class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch.lower() in 'aeiou']
        vowels.reverse()

        result = []
        for ch in s:
            if ch.lower() in 'aeiou':
                result.append(vowels.pop(0))
            else:
                result.append(ch)
        return ''.join(result)
        