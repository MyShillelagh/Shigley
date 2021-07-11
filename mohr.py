#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


def circleplot(rad, center_x, center_y):
    theta = np.linspace(0, 2 * np.pi, 100)
    x_vals = rad * np.cos(theta) + center_x
    y_vals = rad * np.sin(theta) + center_y
    graph = plt.plot(x_vals, y_vals)
    graph.set_xlabel('Stress')
    graph.set_ylabel('Torque')
    graph.invert_yaxis()
    return graph


def centerrad(stress1, stress2):
    rad = np.sqrt((stress1[0] ** 2 - stress2[0] ** 2) +
                  (stress1[1] ** 2 - stress2[1] ** 2)) / 2
    center = (stress1 + stress2) / 2
    return rad, center


if __name__ == "__main__":
    print('Hello, world!')
