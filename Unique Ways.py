class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        m is length
        n is width
        """
        grid = [[0] * (n+1) for _ in range(m+1)]
        grid[-2][-2] = 1
        print(grid)
        for n_index in range(n-1, -1, -1):
            for m_index in range(m-1, -1, -1):
                if m_index == m-1 and n_index == n-1:
                    continue
                else:
                    grid[m_index][n_index] = grid[m_index + 1][n_index] + grid[m_index][n_index + 1]
        return grid[0][0]
