n = int(input("Enter number of queens: "))

board = [[0] * n for _ in range(n)]

# Arrays for Branch and Bound optimization
columns = [False] * n
leftDiagonal = [False] * (2 * n)
rightDiagonal = [False] * (2 * n)


def solve(row):
    # If all queens are placed
    if row == n:
        print("\nSolution Found:\n")

        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

        return True

    # Try placing queen in every column
    for col in range(n):

        # Branch and Bound checking
        if (not columns[col] and
                not leftDiagonal[row - col + n] and
                not rightDiagonal[row + col]):

            # Place queen
            board[row][col] = 1

            # Mark column and diagonals as occupied
            columns[col] = True
            leftDiagonal[row - col + n] = True
            rightDiagonal[row + col] = True

            # Recur for next row
            if solve(row + 1):
                return True

            # Backtracking
            board[row][col] = 0
            columns[col] = False
            leftDiagonal[row - col + n] = False
            rightDiagonal[row + col] = False

    return False


if not solve(0):
    print("No solution exists")
