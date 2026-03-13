import numpy as np

def convert_to_array(s):
    """
    Convert string representation of result column into numpy array
    """
    s_clean = s.replace("\n", " ").strip().strip("[]")
    return np.fromstring(s_clean, sep=" ")


def stack_results(series):
    """
    Convert result column to matrix
    """
    return np.vstack(series.values)