"""
Using Associative arrays we can provide one-to-one key-value mappings that are faster than a series
of if-else statements. (Switch-Statements)
"""


def switch_1(argument):
    switcher = {
        1: "Jan.",
        2: "Feb.",
        3: "Mar.",
        4: "Apr.",
        5: "May",
        6: "Jun.",
        7: "Jul.",
        8: "Aug.",
        9: "Sep.",
        10: "Oct.",
        11: "Nov.",
        12: "Dec."
    }
    print(switcher.get(argument, "Invalid Month"))

switch_1(1)
"""
Using the same style of mapping we can use switch-statements for defined functions as well.
(For the sake of time only 5 months are in this switch-statement 
"""


def one():
    return "Jan."
def two():
    return "Feb."
def three():
    return "Mar."
def four():
    return "Apr."
def five():
    return "May"


def switch_2(argument):
    switcher = {
        1: one,
        2: two,
        3: three(),
        4: four,
        5: five,
    }
    func = switcher.get(argument, lambda: "Invalid month")
    print(func())

switch_2(2)

"""
using the same method we can do the same with class-objects to create switch-statements
"""

class Months(object):
    def switch_3(self,argument):
        method_name = 'month_' + str(argument)
        # get the method from 'self'. Default it to lambda.
        method = getattr(self, method_name, lambda: "Invalid month.")
        # call the method as we return it
        return method()

    def month_1(self):
        return "Jan."

    def month_2(self):
        return "Feb."

    def month_3(self):
        return "Mar."

    def month_4(self):
        return "Apr."

a = Months()
print(a.switch_3(3))

