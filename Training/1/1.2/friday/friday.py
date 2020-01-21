"""
ID: dotekin1
LANG: PYTHON3
TASK: friday
"""
def months_of(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    else:
        return (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

with open("friday.in") as fin:
    N = int(fin.read().strip())
    
counts = [0] * 7
day = 0
for year in range(1900, 1900 + N):
    for month in months_of(year):
        counts[day] += 1
        day = (day + month) % 7

with open("friday.out", "w") as fout:
    fout.write(' '.join(map(str, counts)) + '\n')