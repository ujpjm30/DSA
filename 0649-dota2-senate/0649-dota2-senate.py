class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R = []
        D = []
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        from collections import deque
        R = deque(R)
        D = deque(D)

        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        return "Radiant" if R else "Dire"
