import calendar

def solve(value):
    return calendar.monthrange(value[0], value[1])[1]
