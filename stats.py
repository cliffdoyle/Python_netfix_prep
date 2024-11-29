"""measure of central tendency"""

import statistics

grades=[85,93,45,89,85]

print(sorted(grades))

print(statistics.mean(grades))
print(statistics.median(grades))
print(statistics.mode(grades))

for ch in range(78):
    print(ch)