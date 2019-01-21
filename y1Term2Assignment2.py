# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, no-member, C0301, C0411, W0511

''' Term 2, Assignment 2

Assignment Tasks: 4

Restrictions:
    Do not change anything outside TODO blocks.
    Do not add pylint directives.

Guidance:
    Define a function to generate random numbers with a PDF reflecting
    the angular intensity distribution behind a single slit and generate
    a plot comparing the histogram of a drawn sample with the PDF. The angular
    range is -pi/2 to pi/2.

    Ensure that your program correctly evaluates sin(x)/x at x=0, which should
    yield 1.

    Task 2:
    Ensure that the PDF is normalized.

Author of template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''


import numpy as np
import scipy.interpolate as interpolate
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Fixed wavelength and slit_width in metres
wavelength = 500e-9
slit_width = 1500e-9

# TODO: Assignment Task 1: define any additional functions you might need
pass
# End of Task 1; proceed to task 2.

def slit_pdf(alpha):
    """ Calculate the value of the pdf at angles alpha

    Parameters
    ----------
    alpha : float or numpy array of float
        angle(s) to evaluate the pdf at.
        angles are in radians.

    Returns
    -------
    pdf_values: float or numpy array of float
        resulting value(s) of the pdf
    """
    # TODO: Assignment Task 2: write function body
    pass
    # End of Task 2; proceed to task 3.

def rv_from_pdf(pdf_function, pdf_range, n):
    """ Calculate random values with given pdf

    Parameters
    ----------
    pdf_function : function
        The PDF function

    pdf_range : array-like
        pdf_range[0] is the allowed minimum value for the random values
        pdf_range[1] is the allowed maximum value for the random values

    n : integer
        number of random values to draw

    Returns
    -------
    rv: numpy array of float
        resulting random values
    """
    # TODO: Assignment Task 3: write function body
    pass
    # End of Task 3; proceed to task 4.

def generate_plot(fig, n, bins):
    """ Create a fully labelled plot

    Plot a histogram with error bars overlayed by the PDF.

    Parameters
    ----------

    fig: matplotlib figure
        object to draw on

    n: integer
        number of samples to use to generate the histogram

    bins: integer
        number of bins to use to generate the histogram

    Returns
    -------
    fig: matplotlib figure
        figure object with fully labelled plot
    """
    # TODO: Assignment Task 4: write function body
    pass
    # End of Task 4; no further tasks.

def main():
    ''' do everything '''
    fig = plt.figure()
    fig = generate_plot(fig, 10000, 51)
    plt.show()


if __name__ == '__main__':
    main()
