class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R = deque(i for i, c in enumerate(senate) if c == 'R')
        D = deque(i for i, c in enumerate(senate) if c == 'D')

        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        return "Radiant" if R else "Dire"
        