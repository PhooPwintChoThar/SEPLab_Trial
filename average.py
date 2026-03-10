def printIt(x):
    print(x, end='-')
    return True


def findAverage(listValues: list[int], minimum: int = 0, maximum: int = 10) -> float:
    printIt(1)
    i = 1
    total_input = total_valid = 0
    sum = 0.0

    while (i <= len(listValues) and printIt(2) and listValues[i-1] != -999 and
           printIt(3) and total_input < 10):

        printIt(4)
        total_input += 1

        if (printIt(5) and minimum <= listValues[i-1] and
                printIt(6) and listValues[i-1] <= maximum):

            printIt(7)
            total_valid += 1
            sum += listValues[i-1]

        printIt(8)
        i += 1
        printIt(9)

    # end while

    if printIt(10) and total_valid > 0:
        printIt(11)
        average = sum / total_valid
    else:
        printIt(12)
        average = -999

    printIt(13)
    return average