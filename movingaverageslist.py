class MovingAveragesList(object):

    """
    This class implements a list to which numeric values can be appended.
    Doing so actually appends a dictionary containing three values:

    "value" - the value added

    "average" - the arithmetic mean of all values up to and
    including the current one

    "movingaverage" - the arithmetic mean of the specified
    number of previous values

    The underlying list can be accessed using objectname.data.
    """

    def __init__(self, points):

        """
        The points argument specifies how many previous values
        should be used to calculate each moving average.
        """

        self.data = []
        self.points = points


    def append(self, n):

        """
        Adds a dictionary of value, overall average and moving average
        to the list.
        """

        average = self.__calculate_overall_average(n)
        moving_average = self.__calculate_moving_average(n)
        self.data.append({"value": n,
                          "average": average,
                          "movingaverage": moving_average})


    def __calculate_overall_average(self, n):

        length = len(self.data)

        if length == 0:
            average = n
        else:
            average = (((self.data[length - 1]["average"]) *
                         length) + n) / (length + 1)

        return average


    def __calculate_moving_average(self, n):

        length = len(self.data)

        if length == 0:
            moving_average = n
        elif length <= self.points - 1:
            moving_average = (((self.data[length - 1]["average"]) *
                                length) + n) / (length + 1)
        else:
            moving_average = ((self.data[length - 1]["movingaverage"] * self.points) -
                              (self.data[length - self.points]["value"]) + n) / self.points

        return moving_average


    def __str__(self):

        """
        Create a grid from the data in the list.
        """

        items = []

        items.append("-" * 49 + "\n")
        items.append("|          value|overall average| moving average|\n")
        items.append("-" * 49 + "\n")

        for item in self.data:
            items.append("|{:15.2f}|{:15.2f}|{:15.2f}|\n"
                        .format(item["value"], item["average"], item["movingaverage"]))

        items.append("-" * 49)

        return "".join(items)
