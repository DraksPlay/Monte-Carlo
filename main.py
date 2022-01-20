# Calculating the area using the Monte-Carlo method

import random


def Circle(x0, y0, r):
    xmin = x0 - r
    xmax = x0 + r
    ymin = y0 - r
    ymax = y0 + r

    N = 1000000

    inArea = 0

    for i in range(0, N):

        x = xmin + (xmax - xmin) * random.uniform(0.0, 1.0)
        y = ymin + (ymax - ymin) * random.uniform(0.0, 1.0) 

        if ((x-x0)**2 + (y-y0)**2) < r*r:
            inArea += 1

    return inArea/N * (xmax-xmin) * (ymax-ymin)

print(Circle(2, 2, 2))
