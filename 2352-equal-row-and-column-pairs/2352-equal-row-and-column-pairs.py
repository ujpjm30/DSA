class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_count = {}
        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) +1

        count= 0
        for c in range(n):
            col_tuple = tuple(grid[r][c] for r in range(n))
            if col_tuple in row_count:
                count += row_count[col_tuple]

        return count