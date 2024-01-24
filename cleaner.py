import random
from datetime import datetime

n = int(input('Enter the n value: '))
room = [[random.choice([0, 1]) for _ in range(n)] for _ in range(n)]

cleaned = sum(row.count(1) for row in room)
s = datetime.now()

for i in range(n):
    for j in range(n):
        if room[i][j] == 1:
            print(f'Dirty at {i} and {j}')
            room[i][j] = 0

e = datetime.now()

print(f'Performance of vacuum cleaner is: {(cleaned) / (n**2) * 100}')
print(f'Time taken is: {(e - s)}')
