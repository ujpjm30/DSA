class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        w = 0
        i = 0

        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1

            chars[w] = chars[i]
            w += 1

            cnt = j - i
            if cnt > 1:
                for c in str(cnt):
                    chars[w] = c
                    w += 1

            i = j

        return w
            