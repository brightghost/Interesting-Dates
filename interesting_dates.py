from datetime import *
from sys import argv

print()
# the lazy way to process a flag...
if len(argv) > 1 and \
(argv[1] == "-l" or \
argv[1] == "--leapyear"):
    startDate = date(2012,1,1) - timedelta(days=1)
    print("Calculating interesting DoY/DoM divisors for a leap year")
else:
    # start one day before the start of the year...
    startDate = date(2013,1,1) - timedelta(days=1)
    print("Calculating interesting DoY/DoM divisors for a normal year")

print()
print("DoY", "\t", "Mo.", "\t", "Day", "\t", "Interesting divisor")
print("===", "\t", "===", "\t", "===", "\t", "===", "\t", "===")

for i in range(1, 366):
    currentDelta = timedelta(days=i)
    currentDate = startDate + currentDelta
    isInteresting = False
    remainder = currentDelta.days % currentDate.day
    divisor = currentDelta.days / currentDate.day

    if remainder == 0 and \
    divisor != currentDelta.days and \
    divisor != 1:
        isInteresting = "*"
    if divisor == 10:
        isInteresting = "***"
    if isInteresting is False:
        # clear the fields if we don't care about the date
        divisor = ""
        isInteresting = ""
    else:
        # convert the divisor to int for cleaner display
        divisor = int(divisor)
    print(currentDelta.days, "\t", \
        currentDate.strftime("%b"), "\t", \
        currentDate.day, "\t", \
        isInteresting, "\t", \
        divisor
        )

