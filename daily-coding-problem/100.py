"""You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (3, 4)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2). """

import math

def get_distance(input):
    dist = 0
    for iterator in range(1, len(input)):
        row_dist = abs(input[iterator][0] - input[iterator - 1] [0])
        col_dist = abs(input[iterator][1] - input[iterator - 1] [1])
        dist += max(row_dist, col_dist)

    return dist

input = [(0, 0), (1, 1), (3, 4)]

print(get_distance(input))