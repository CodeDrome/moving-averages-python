import random

import movingaverageslist


def main():

    print("-------------------")
    print("| codedrome.com   |")
    print("| Moving Averages |")
    print("-------------------\n")

    response_times_ms = populate_response_times()
    print(response_times_ms)

    # Quick demo of accessing the list directly.
    print(response_times_ms.data[-1])


def populate_response_times():

    """
    Create a MovingAveragesList object and populate it with
    random response times.
    """

    response_times_ms = movingaverageslist.MovingAveragesList(4)

    # Add a large number of normal times
    for t in range(1, 996):
        response_times_ms.append(random.randint(10, 50))

    # Add a few excessively long times
    for t in range(1, 6):
        response_times_ms.append(random.randint(100, 500))

    return response_times_ms


main()
