def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        memo = []
        for x in range(m):
            new_row = []
            for y in range(n):
                new_row.append(0)
            memo.append(new_row)

        for i in range(m):
            memo[i][0] = 1

        for j in range(n):
            memo[0][j] = 1

        for row in range(1, m):
            for col in range(1, n):
                memo[row][col] = memo[row - 1][col] + memo[row][col - 1]

        return memo[m - 1][n - 1]
