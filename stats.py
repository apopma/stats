from math import sqrt
__author__ = 'Adam'
# Stats for Python 3.4.2

class Stats(object):
    # Syntax: Stats([foo, bar, ...]).function()

    def __init__(self, numbers):
        self.numbers = numbers
        self.sanity_check = True
                                                                # Some basic sanity testing:
        if len(self.numbers) <= 0:                              # First be sure you have a list
            print ("Error: Stats was passed an empty list!")
            self.sanity_check = False

        for x in range(len(self.numbers)):                      # Then be sure everything's an int or a float
            if type(self.numbers[x]) is not int and type(self.numbers[x]) is not float:
                try:
                    self.numbers[x] = float(self.numbers[x])    # Try to float anything that isn't a float
                except ValueError:                              # If you can't, fail the sanity test
                    print ("Error: Stats was passed something that isn\'t a number!")
                    self.sanity_check = False

        if self.sanity_check:
            print("Input passed sanity check, continuing...")


    def avg(self):
        # Takes a list of numbers and returns the arithmetic mean

        if not self.sanity_check:
            print("'avg' failed sanity check, aborting")
            return None

        return sum(self.numbers) / len(self.numbers)


    def stdev(self):
        # Takes a list of numbers and returns standard deviation

        if not self.sanity_check:
            print("'stdev' failed sanity check, aborting")
            return None

        original_mean = self.avg()
        diff = []

        for x in self.numbers : diff.append ((x - original_mean) ** 2)
        new_mean = sum(diff) / len(diff) # This could call .avg() but it's honestly easier just to duplicate it
        return sqrt(new_mean)


    def median(self):
        # Takes a list of numbers and returns its median,
        # averaging the middle two indices if the list isn't of odd length

        if not self.sanity_check:
            print ("'median' failed sanity check, aborting")
            return None

        new_list = []
        if len(self.numbers) % 2 == 0:                       # for lists of even length:
            new_list = sorted(self.numbers)
            middle1 = new_list[len(new_list) // 2]           # Gets the middle two indices of the list
            middle2 = new_list[(len(new_list) // 2) - 1]     # Needs to be floor-divided so that it gets int for index

            return (middle1 + middle2) / 2.0                 # just to be perfectly bloody sure it returns a float

        elif len(self.numbers) % 2 != 0:
            new_list = sorted(self.numbers)                  # for lists of odd length:
            return float(new_list[len(new_list) // 2 ])      # Just returns the middle index as a float


    def cv(self):
        # Takes a list of numbers and returns coefficient of variation: standard deviation over mean

        if not self.sanity_check:
            print ("'cv' failed sanity check, aborting")
            return None

        return self.stdev() / self.avg()