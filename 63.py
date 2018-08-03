from collections import defaultdict


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)  # rows
        n = len(obstacleGrid[0])  # cols
        A = defaultdict(lambda: defaultdict(lambda: 0))
        A[n - 1][m - 1] = 1 if obstacleGrid[m - 1][n - 1] == 0 else 0
        for start_x in range(n - 2, -m, -1):
            for i, y in enumerate(range(m - 1, -1, -1)):
                x = start_x + i
                if x >= n or x < 0 or obstacleGrid[y][x] == 1:
                    continue
                if x + 1 < n and obstacleGrid[y][x + 1] == 0:
                    A[x][y] += A[x + 1][y]
                if y + 1 < m and obstacleGrid[y + 1][x] == 0:
                    A[x][y] += A[x][y + 1]
        return A[0][0]


if __name__ == "__main__":
    grid = [[1, 0]]
    print(Solution().uniquePathsWithObstacles(grid))
