
if __name__ == "__main__":
    num_tests = int(input())
    for test in range(num_tests):
        numbers = list(map(int, list(input())))

        result = ""
        parenthesis_count = 0
        for number in numbers:
            while parenthesis_count < number:
                result += "("
                parenthesis_count += 1

            while number < parenthesis_count:
                result += ")"
                parenthesis_count -= 1

            result += str(number)

        while 0 < parenthesis_count:
            result += ")"
            parenthesis_count -= 1

        print("Case #" + str(test + 1) + ": " + result)
