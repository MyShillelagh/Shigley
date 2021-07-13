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
    graph = plt.plot(x_vals, y_vals)
    graph.set_xlabel('Stress')
    graph.set_ylabel('Torque')
    # Gotta invert the y axis for a proper Mohr's circle
    graph.invert_yaxis()
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
    theta = np.linspace(0, 2 * np.pi, 1000)
    x_vals = rad * np.cos(theta) + center[0]
    y_vals = rad * np.sin(theta) + center[1]
    return x_vals, y_vals


if __name__ == "__main__":
    stress1 = np.array([20, -10])
    stress2 = np.array([5, 10])
    testrad, testcenter = centerrad(stress1, stress2)
    test_x, test_y = circlepoints(testrad, testcenter)
    plt.plot(test_x, test_y)
    plt.show()

