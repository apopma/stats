from math import sqrt
__author__ = 'Adam'
# Stats for Python 3.4.2

class Stats(object):
    # Syntax: Stats(x).function(), where x is a list of integers or floats

    def __init__(self, numbers):
        self.numbers = numbers


    def avg(self):
        # Takes a list of numbers and returns the arithmetic mean

        if type(self.numbers) != list: return "Wrong type"
        return sum(self.numbers) / len(self.numbers)


    def stdev(self):
        # Takes a list of numbers and returns standard deviation
        # Std. dev is the square root of the average of squared differences of each value from the mean
        # First get the original mean, then calculate difference of each data point from it, then square that value
        # Then get the mean of those values and square root it

        original_mean = self.avg()
        diff = []

        for x in self.numbers : diff.append ((x - original_mean) ** 2)
        new_mean = sum(diff) / len(diff) # This could call .avg() but it's honestly easier just to duplicate it
        return sqrt(new_mean)


    def cv(self):
        # Takes a list of numbers and returns coefficient of variation: standard deviation over mean
        return self.stdev() / self.avg()
