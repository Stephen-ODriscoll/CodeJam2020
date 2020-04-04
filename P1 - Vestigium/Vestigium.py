
if __name__ == "__main__":
    num_tests = int(input())
    for test in range(num_tests):
        matrix = []
        size = int(input())
        for _ in range(size):
            matrix.append(list(map(int, input().split())))

        diagonal = sum(matrix[i][i] for i in range(size))

        row_duplicates = 0
        for i in range(size):
            if len(set(matrix[i])) != size:
                row_duplicates += 1

        col_duplicates = 0
        for i in range(size):
            if len(set(row[i] for row in matrix)) != size:
                col_duplicates += 1

        print("Case #" + str(test + 1) + ": " + str(diagonal) + " " + str(row_duplicates) + " " + str(col_duplicates))
