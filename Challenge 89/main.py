'''
1
5 4
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
'''
import os
os.system("cls")

matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0],
]

columns, rows = [5, 4]

count = 0
for row in range(rows):
    for column in range(columns):
        if not matrix[row][column]:
            continue

        count += 1
        # if(row == 0):


print(count)
