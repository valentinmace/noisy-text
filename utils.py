# Valentin Mace
# valentin.mace@kedgebs.com
# Developed at Qwant Research

"""Tools"""

import random


def random_bool(probability=0.5):
    """Returns True with given probability

    Args:
        probability: probability to return True

    """
    assert (0 <= probability <= 1), "probability needs to be >= 0 and <= 1"
    return random.random() < probability


def count_lines(filename):
    """Returns the number of lines in the given file

    Args:
        filename: (string) path to the file

    """
    return sum(1 for line in open(filename))
