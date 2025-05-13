# Recursive memoized DP
def _min_path(grid, r, c, m):
	if r == len(grid) or c == len(grid[0]): # or grid[r][c] == "w" for blocked grids
		return float("inf")

	if r == len(grid)-1 and c == len(grid[0])-1:
		return grid[r][c]

	pos = (r,c)

	if pos in m:
		return m[pos]

	down_min_path = _min_path(grid, r+1, c, m)
	right_min_path = _min_path(grid, r, c+1, m)

	m[pos] = grid[r][c] + min(down_min_path, right_min_path)

	return grid[r][c] + min(down_min_path, right_min_path)

def min_path_rec(grid):
	return _min_path(grid, 0, 0, {})

# Iterative 2D DP
def min_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a dp grid initialized to 0 with same dimensions
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Start from the bottom-right corner
    for r in reversed(range(rows)):
        for c in reversed(range(cols)):
            if r == rows - 1 and c == cols - 1:
                dp[r][c] = grid[r][c]
            elif r == rows - 1:
                dp[r][c] = grid[r][c] + dp[r][c + 1]  # Only right move possible
            elif c == cols - 1:
                dp[r][c] = grid[r][c] + dp[r + 1][c]  # Only down move possible
            else:
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])  # Both moves possible
                
    return dp[0][0]