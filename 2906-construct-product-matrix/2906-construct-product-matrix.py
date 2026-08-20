class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD= 12345
        n=len(grid)
        m=len(grid[0])
        p= [[1]*m for _ in range(n)]
        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD
        suffix = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                p[i][j] = (p[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
        return p