# input
day, month = input().split(' ')
day, month = int(day), int(month)
# data
daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# counters
currentDay = 2
totalDays = sum(daysInMonth[ 0 : (month-1) ]) if month != 1 else 0
totalDays += day
final = days[ (totalDays+2) % len(days) ]
print(final)