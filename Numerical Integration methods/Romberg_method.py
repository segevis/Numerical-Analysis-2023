import math

import numpy as np
from colors import bcolors


def romberg_integration(func, a, b, n):
    """
    Romberg Integration

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of iterations (higher value leads to better accuracy).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    h = b - a
    R = np.zeros((n, n), dtype=float)

    R[0, 0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, n):
        h /= 2
        sum_term = 0

        for k in range(1, 2 ** i, 2):
            sum_term += func(a + k * h)

        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_term

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4 ** j) - 1)

    return R[n - 1, n - 1]


def f(x):
    return (math.cos(x) + (x ** 3 - x + 2)) / (2 * math.e ** (-x + 2))


if __name__ == '__main__':
    a = -1.1
    b = 0.7
    n = 20
    integral = romberg_integration(f, a, b, n)
    # print(f" Division into n={n} sections ")
    print(f"{bcolors.OKBLUE}Approximate integral in range [{a},{b}] is {integral:.5f}{bcolors.ENDC}"," n = ",n)
