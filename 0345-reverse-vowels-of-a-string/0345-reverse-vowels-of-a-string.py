class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch.lower() in 'aeiou':
                vowels.append(ch)

        vowels.reverse()

        result = []
        v_idx = 0
        for ch in s:
            if ch.lower() in 'aeiou':
                result.append(vowels[v_idx])
                v_idx += 1
            else: 
                result.append(ch)
        return "".join(result)
        