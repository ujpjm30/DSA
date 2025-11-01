class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = Counter(tuple(row) for row in grid)
        cols = Counter(tuple(col) for col in zip(*grid))
        ans = 0
        for t, rc in rows.items():
            ans += rc * cols.get(t, 0)
        return ans