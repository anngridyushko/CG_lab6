import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math
import numpy as np

x = [[15, 15, 15, 15, 15, 15],
     [0,  0,  8,  8, 4, 4],
     [0, 20, 20, 16, 18, 0]]

x[1] = [i + 20 for i in x[1]]

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')


def move(delta):
    x[0] = [i + delta for i in x[0]]


def draw():
    for i in range(300):
        x[0] = [k - 0.01 for k in x[0]]
        vertices = [list(zip(x[0], x[1], x[2]))]
        poly = Poly3DCollection(vertices, alpha=0.1)

        ax.add_collection3d(poly)


def rotare(delta, x):
    matrix = [[1, 0, 0],
              [0, math.cos(delta), -1 * math.sin(delta)],
              [0, math.sin(delta), math.cos(delta)]]
    return np.dot(matrix, np.array(x))

def drawYZ():
    for i in range(300):
        x[0] = [k + 0.01 for k in x[0]]
        vertices = [list(zip([0 for i in x[2]], x[1], x[2]))]
        poly = Poly3DCollection(vertices, alpha=0.1)
        poly.set_color('g')
        ax.add_collection3d(poly)


def drawXY():
    for i in range(300):
        x[0] = [k + 0.01 for k in x[0]]
        vertices = [list(zip(x[0], x[1], [0 for i in x[2]]))]
        poly = Poly3DCollection(vertices, alpha=0.1)
        poly.set_color('g')
        ax.add_collection3d(poly)

def drawXZ():
    for i in range(300):
        x[0] = [k + 0.01 for k in x[0]]
        vertices = [list(zip(x[0], [60 for i in x[2]], x[2]))]
        poly = Poly3DCollection(vertices, alpha=0.1)
        poly.set_color('g')
        ax.add_collection3d(poly)



draw()

move(25)
x = rotare(0.5, x)
draw()

ax.set_xlim(0,70)

ax.set_ylim(0,70)

ax.set_zlim(0,70)

move(25)
drawXY()
drawXZ()
drawYZ()

plt.show()