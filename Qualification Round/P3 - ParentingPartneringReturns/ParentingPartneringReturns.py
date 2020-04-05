
if __name__ == "__main__":
    num_tests = int(input())
    for test in range(num_tests):
        activities = []
        num_activities = int(input())
        for i in range(num_activities):
            activities.append(list(map(int, input().split())) + [i])

        activities.sort(key=lambda x: x[0])

        C, J = 0, 0
        impossible = False
        for activity in activities:
            if C <= activity[0]:
                C = activity[1]
                activity.append(0)
            elif J <= activity[0]:
                J = activity[1]
                activity.append(1)
            else:
                impossible = True
                break

        result = ""
        if impossible:
            result = "IMPOSSIBLE"
        else:
            activities.sort(key=lambda x: x[2])
            for activity in activities:
                if activity[3] == 0:
                    result += "C"
                else:
                    result += "J"

        print("Case #" + str(test + 1) + ": " + result)
