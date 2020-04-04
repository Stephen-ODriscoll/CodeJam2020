import numpy as np


def main():
    num_tests = int(input())
    for test in range(num_tests):
        size, trace_goal = list(map(int, input().split()))
        combinations = get_combinations(size, trace_goal)

        possible, matrix = False, np.array([])
        for combination in combinations:
            matrix = np.array([[0 for _ in range(size)] for _ in range(size)])
            for i in range(size):
                matrix[i][i] = combination[i]

            if combination_possible(matrix, size):
                possible = True
                break

        if possible:
            print("Case #" + str(test + 1) + ": POSSIBLE")
            print('\n'.join(' '.join(str(elem) for elem in row) for row in matrix))
        else:
            print("Case #" + str(test + 1) + ": IMPOSSIBLE")


def get_combinations(size, goal):
    combinations = []
    combination = [1 for _ in range(size)]

    index = 0
    while index < size:
        index = 0
        if sum(combination) == goal:
            combinations.append(combination.copy())

        while index < size <= combination[index]:
            combination[index] = 1
            index += 1
        if index < size:
            combination[index] += 1

    return combinations


def combination_possible(matrix, size):
    additions = []
    backtrack = False

    x = 0
    while x < size:
        y = 0
        while y < size:
            if not backtrack and matrix[x][y] != 0:
                y += 1
                continue

            backtrack = False
            elem = matrix[x][y]
            while elem == 0 or elem in matrix[x] or elem in matrix[:, y]:
                elem += 1
                if size < elem:
                    if 0 < len(additions):
                        x, y, _ = additions.pop(-1)
                        backtrack = True
                        break
                    else:
                        return False

            if not backtrack:
                matrix[x][y] = elem
                additions.append((x, y, elem))
                y += 1
        x += 1

    return True


if __name__ == "__main__":
    main()
