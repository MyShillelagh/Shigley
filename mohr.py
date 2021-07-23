#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


def circleplot(stress1, stress2):
    """
    Plots a Mohr's circle based on stresses
    :param stress1: The first stress experienced by the element
    :param stress2: The second stress experienced by the element
    :return: A graph of the circle
    """
    rad, center = centerrad(stress1, stress2)
    x_vals, y_vals = circlepoints(rad, center)
    graph = plt.figure()
    ax = graph.add_subplot()
    ax.plot(x_vals, y_vals)
    ax.set_xlabel('Stress')
    ax.set_ylabel('Torque')
    ax.axis('equal')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    # Gotta invert the y axis for a proper Mohr's circle
    ax.invert_yaxis()
    return graph


def centerrad(stress1, stress2):
    """
    ADD HELPFUL COMMENTS HERE
    """
    rad = np.sqrt((stress1[0] ** 2 - stress2[0] ** 2) +
                  (stress1[1] ** 2 - stress2[1] ** 2)) / 2
    center = (stress1 + stress2) / 2
    return rad, center


def circlepoints(rad, center):
    """
    Gives x and y values of a circle with a given radius and center
    :param rad: Radius of circle
    :param center: Location of center of circle in form [x, y]
    :return: x and y values that can be used to plot circle
    """
    theta = np.linspace(0, 2 * np.pi, 1000)
    x_vals = rad * np.cos(theta) + center[0]
    y_vals = rad * np.sin(theta) + center[1]
    return x_vals, y_vals


if __name__ == "__main__":
    stress1 = np.array([20, -10])
    stress2 = np.array([5, 10])
    graph = circleplot(stress1, stress2)
    graph.savefig('test.png')
