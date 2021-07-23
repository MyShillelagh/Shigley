#! /usr/bin/python3

import numpy as np


def vonmises(stress1, stress2, stress3):
    return np.sqrt(((stress1 - stress2)**2 +
                    (stress1 - stress3)**2 +
                    (stress2 - stress3)**2) / 2)
