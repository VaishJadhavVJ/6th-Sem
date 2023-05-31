def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]  # Initialize an empty n x n board
    solutions = []  # List to store all valid solutions

    def is_safe(row, col):
        # Check if it is safe to place a queen at position (row, col)
        for i in range(row):
            if board[i][col] == 'Q':  # Check if there is a queen in the same column
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':  # Check upper left diagonal
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':  # Check upper right diagonal
                return False
        return True

    def backtrack(row):
        if row == n:  # Found a valid solution
            solutions.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'  # Place a queen at position (row, col)
                backtrack(row + 1)  # Move to the next row
                board[row][col] = '.'  # Remove the queen to explore other possibilities

    backtrack(0)  # Start backtracking from the first row
    return solutions

# Example usage:
n = int(input("Enter the number of queens: "))
solutions = solve_n_queens(n)
print("Number of solutions:", len(solutions))
for i, solution in enumerate(solutions):
    print("Solution", i + 1)
    for row in solution:
        print(row)
    print()
