import numpy as np


# 0 = empty rectangle, 1 = dot, 2 = big dot, 3 = gate 4 = vertical line,
# 5 = horizontal line, 6 = top right, 7 = top left, 8 = bot right, 9 = bot left

level1 = np.array([
[7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
[4, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 1, 7, 5, 5, 6, 1, 7, 5, 5, 5, 6, 1, 4, 4, 1, 7, 5, 5, 5, 6, 1, 7, 5, 5, 6, 1, 4, 4],
[4, 4, 2, 4, 0, 0, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 0, 0, 4, 2, 4, 4],
[4, 4, 1, 9, 5, 5, 8, 1, 9, 5, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 5, 8, 1, 9, 5, 5, 8, 1, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 1, 7, 5, 5, 6, 1, 7, 6, 1, 7, 5, 5, 5, 5, 5, 5, 6, 1, 7, 6, 1, 7, 5, 5, 6, 1, 4, 4],
[4, 4, 1, 9, 5, 5, 8, 1, 4, 4, 1, 9, 5, 5, 6, 7, 5, 5, 8, 1, 4, 4, 1, 9, 5, 5, 8, 1, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 9, 5, 5, 5, 5, 6, 1, 4, 9, 5, 5, 6, 0, 4, 4, 0, 7, 5, 5, 8, 4, 1, 7, 5, 5, 5, 5, 8, 4],
[9, 5, 5, 5, 5, 6, 4, 1, 4, 7, 5, 5, 8, 0, 9, 8, 0, 9, 5, 5, 6, 4, 1, 4, 7, 5, 5, 5, 5, 8],
[0, 0, 0, 0, 0, 4, 4, 1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 1, 4, 4, 0, 0, 0, 0, 0],
[5, 5, 5, 5, 5, 8, 4, 1, 4, 4, 0, 7, 5, 5, 3, 3, 5, 5, 6, 0, 4, 4, 1, 4, 9, 5, 5, 5, 5, 5],
[5, 5, 5, 5, 5, 5, 8, 1, 9, 8, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 9, 8, 1, 9, 5, 5, 5, 5, 5, 5],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[5, 5, 5, 5, 5, 5, 6, 1, 7, 6, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 7, 6, 1, 7, 5, 5, 5, 5, 5, 5],
[5, 5, 5, 5, 5, 6, 4, 1, 4, 4, 0, 9, 5, 5, 5, 5, 5, 5, 8, 0, 4, 4, 1, 4, 7, 5, 5, 5, 5, 5],
[0, 0, 0, 0, 0, 4, 4, 1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 1, 4, 4, 0, 0, 0, 0, 0],
[7, 5, 5, 5, 5, 8, 4, 1, 4, 4, 0, 7, 5, 5, 5, 5, 5, 5, 6, 0, 4, 4, 1, 4, 9, 5, 5, 5, 5, 6],
[4, 7, 5, 5, 5, 5, 8, 1, 9, 8, 0, 9, 5, 5, 6, 7, 5, 5, 8, 0, 9, 8, 1, 9, 5, 5, 5, 5, 6, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 1, 7, 5, 5, 6, 1, 7, 5, 5, 5, 6, 1, 4, 4, 1, 7, 5, 5, 5, 6, 1, 7, 5, 5, 6, 1, 4, 4],
[4, 4, 1, 9, 5, 6, 4, 1, 9, 5, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 5, 8, 1, 4, 7, 5, 8, 1, 4, 4],
[4, 4, 2, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 2, 4, 4],
[4, 9, 5, 6, 1, 4, 4, 1, 7, 6, 1, 7, 5, 5, 5, 5, 5, 5, 6, 1, 7, 6, 1, 4, 4, 1, 7, 5, 8, 4],
[4, 7, 5, 8, 1, 9, 8, 1, 4, 4, 1, 9, 5, 5, 6, 7, 5, 5, 8, 1, 4, 4, 1, 9, 8, 1, 9, 5, 6, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 1, 7, 5, 5, 5, 5, 8, 9, 5, 5, 6, 1, 4, 4, 1, 7, 5, 5, 8, 9, 5, 5, 5, 5, 6, 1, 4, 4],
[4, 4, 1, 9, 5, 5, 5, 5, 5, 5, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 5, 5, 5, 5, 5, 5, 8, 1, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8, 4],
[9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8] 
])

level2 = np.array([
[7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
[4, 7, 5, 5, 5, 5, 5, 5, 6, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 5, 5, 5, 5, 5, 5, 6, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 2, 7, 5, 5, 6, 1, 4, 4, 1, 7, 5, 5, 5, 5, 5, 5, 6, 1, 4, 4, 1, 7, 5, 5, 6, 2, 4, 4],
[4, 4, 1, 9, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 5, 5, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 8, 1, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 9, 5, 6, 1, 7, 6, 1, 7, 5, 5, 5, 6, 1, 7, 6, 1, 7, 5, 5, 5, 6, 1, 7, 6, 1, 7, 5, 8, 4],
[9, 5, 6, 4, 1, 4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4, 1, 4, 7, 5, 8],
[5, 5, 8, 4, 1, 4, 4, 1, 9, 5, 5, 5, 8, 1, 4, 4, 1, 9, 5, 5, 5, 8, 1, 4, 4, 1, 4, 9, 5, 5],
[5, 5, 5, 8, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 9, 5, 5, 5],
[0, 0, 0, 0, 1, 4, 9, 5, 5, 6, 0, 7, 5, 5, 8, 9, 5, 5, 6, 0, 7, 5, 5, 8, 4, 1, 0, 0, 0, 0],
[5, 5, 5, 6, 1, 9, 5, 5, 5, 8, 0, 9, 5, 5, 5, 5, 5, 5, 8, 0, 9, 5, 5, 5, 8, 1, 7, 5, 5, 5],
[5, 5, 6, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 7, 5, 5],
[0, 0, 4, 4, 1, 7, 5, 5, 5, 6, 0, 7, 5, 5, 3, 3, 5, 5, 6, 0, 7, 5, 5, 5, 6, 1, 4, 4, 0, 0],
[0, 0, 4, 4, 1, 4, 7, 5, 5, 8, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 9, 5, 5, 6, 4, 1, 4, 4, 0, 0],
[0, 0, 4, 4, 1, 4, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 4, 1, 4, 4, 0, 0],
[5, 5, 8, 4, 1, 4, 4, 0, 7, 6, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 7, 6, 0, 4, 4, 1, 4, 9, 5, 5],
[5, 5, 5, 8, 1, 9, 8, 0, 4, 4, 0, 9, 5, 5, 5, 5, 5, 5, 8, 0, 4, 4, 0, 9, 8, 1, 9, 5, 5, 5],
[0, 0, 0, 0, 1, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 1, 0, 0, 0, 0],
[5, 5, 5, 6, 1, 7, 5, 5, 8, 9, 5, 5, 6, 0, 7, 6, 0, 7, 5, 5, 8, 9, 5, 5, 6, 1, 7, 5, 5, 5],
[5, 5, 6, 4, 1, 9, 5, 5, 5, 5, 5, 5, 8, 0, 4, 4, 0, 9, 5, 5, 5, 5, 5, 5, 8, 1, 4, 7, 5, 5],
[0, 0, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 0, 0],
[7, 5, 8, 4, 1, 7, 5, 5, 5, 6, 0, 7, 5, 5, 8, 9, 5, 5, 6, 0, 7, 5, 5, 5, 6, 1, 4, 9, 5, 6],
[4, 7, 5, 8, 1, 9, 5, 5, 5, 8, 0, 9, 5, 5, 5, 5, 5, 5, 8, 0, 9, 5, 5, 5, 8, 1, 9, 5, 6, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 1, 7, 5, 5, 6, 1, 7, 5, 5, 5, 6, 1, 7, 6, 1, 7, 5, 5, 5, 6, 1, 7, 5, 5, 6, 1, 4, 4],
[4, 4, 1, 4, 0, 0, 4, 1, 4, 7, 5, 5, 8, 1, 4, 4, 1, 9, 5, 5, 6, 4, 1, 4, 0, 0, 4, 1, 4, 4],
[4, 4, 1, 4, 0, 0, 4, 1, 4, 4, 1, 1, 1, 0, 4, 4, 1, 1, 1, 1, 4, 4, 1, 4, 0, 0, 4, 1, 4, 4],
[4, 4, 2, 4, 0, 0, 4, 1, 4, 4, 1, 7, 5, 5, 8, 9, 5, 5, 6, 1, 4, 4, 1, 4, 0, 0, 4, 2, 4, 4],
[4, 4, 1, 9, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 5, 5, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 8, 1, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8, 4],
[9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8] 
])

level3 = np.array([
[7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
[4, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 1, 7, 5, 5, 5, 5, 5, 6, 1, 7, 5, 5, 5, 5, 5, 5, 6, 1, 7, 5, 5, 5, 5, 5, 6, 1, 4, 4],
[4, 4, 2, 9, 5, 5, 5, 5, 6, 4, 1, 4, 7, 5, 5, 5, 5, 6, 4, 1, 4, 7, 5, 5, 5, 5, 8, 2, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 4, 4, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 4, 4, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 9, 5, 5, 5, 5, 6, 1, 4, 4, 1, 4, 4, 1, 7, 6, 1, 4, 4, 1, 4, 4, 1, 7, 5, 5, 5, 5, 8, 4],
[9, 5, 5, 5, 5, 6, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 7, 5, 5, 5, 5, 8],
[0, 0, 0, 0, 0, 4, 4, 1, 9, 8, 1, 9, 8, 1, 4, 4, 1, 9, 8, 1, 9, 8, 1, 4, 4, 0, 0, 0, 0, 0],
[5, 5, 5, 6, 0, 4, 4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 0, 7, 5, 5, 5],
[5, 5, 6, 4, 0, 4, 4, 1, 7, 6, 0, 7, 5, 5, 8, 9, 5, 5, 6, 0, 7, 6, 1, 4, 4, 0, 4, 7, 5, 5],
[0, 0, 4, 4, 0, 9, 8, 1, 4, 4, 0, 9, 5, 5, 5, 5, 5, 5, 8, 0, 4, 4, 1, 9, 8, 0, 4, 4, 0, 0],
[0, 0, 4, 4, 1, 1, 1, 1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 1, 1, 1, 1, 4, 4, 0, 0],
[7, 5, 8, 4, 1, 7, 5, 5, 8, 4, 0, 7, 5, 5, 3, 3, 5, 5, 6, 0, 4, 9, 5, 5, 6, 1, 4, 9, 5, 6],
[4, 7, 5, 8, 1, 9, 5, 5, 5, 8, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 9, 5, 5, 5, 8, 1, 9, 5, 6, 4],
[4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4],
[8, 4, 1, 7, 5, 5, 5, 5, 5, 6, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 7, 5, 5, 5, 5, 5, 6, 1, 4, 9],
[5, 8, 1, 9, 5, 5, 6, 7, 5, 8, 0, 9, 5, 5, 5, 5, 5, 5, 8, 0, 9, 5, 6, 7, 5, 5, 8, 1, 9, 5],
[0, 0, 1, 1, 1, 1, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 1, 1, 1, 1, 0, 0],
[5, 6, 1, 7, 6, 1, 4, 4, 1, 7, 5, 5, 6, 0, 7, 6, 0, 7, 5, 5, 6, 1, 4, 4, 1, 7, 6, 1, 7, 5],
[6, 4, 1, 4, 4, 1, 9, 8, 1, 4, 7, 5, 8, 0, 4, 4, 0, 9, 5, 6, 4, 1, 9, 8, 1, 4, 4, 1, 4, 7],
[4, 4, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 4, 4],
[4, 4, 1, 4, 9, 5, 5, 6, 1, 4, 4, 1, 7, 5, 8, 9, 5, 6, 1, 4, 4, 1, 7, 5, 5, 8, 4, 1, 4, 4],
[4, 4, 1, 9, 5, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 5, 5, 8, 1, 9, 8, 1, 9, 5, 5, 5, 8, 1, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 4, 1, 7, 5, 5, 5, 6, 1, 7, 6, 1, 7, 5, 5, 5, 5, 6, 1, 7, 6, 1, 7, 5, 5, 5, 6, 1, 4, 4],
[4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4, 1, 9, 5, 5, 5, 5, 8, 1, 4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4],
[4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4],
[4, 4, 1, 4, 0, 0, 0, 4, 1, 4, 9, 5, 6, 1, 7, 6, 1, 7, 5, 8, 4, 1, 4, 0, 0, 0, 4, 1, 4, 4],
[4, 4, 2, 9, 5, 5, 5, 8, 1, 9, 5, 5, 8, 1, 4, 4, 1, 9, 5, 5, 8, 1, 9, 5, 5, 5, 8, 2, 4, 4],
[4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
[4, 9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8, 9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8, 4],
[9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8],
])


#levels = {level_count: grid, pac_man_midbottom_position, [spirit positions], get_out_position,,gate for ghosts to come back, ,string_to_display_topleft),
                        #(wall_color, coin_color, gate_color, blink_color)

levels = { 1: (level1, (24, 14.5), [(12,14.5), (15, 14.5) ,(15,12.5), (15,16.5)], (12,14.5),  (16,15), (17,11), ('blue', 'orange', 'white', 'green')), 
           2: (level2, (24, 14.5), [(12,14.5), (15, 14.5) ,(15,12.5), (15,16.5)], (12,14.5),  (16,14), (17,11), ('pink', 'white', 'deeppink', 'floralwhite')),
           3: (level3, (24, 14.5), [(12,14.5), (15, 14.5) ,(15,12.5), (15,16.5)], (12,14.5),  (16,14), (17,11), ('salmon', 'slateblue', 'white', 'gold1'))}



