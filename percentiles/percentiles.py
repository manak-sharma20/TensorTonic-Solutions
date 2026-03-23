import numpy as np
import math


def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x=np.array(x)
    return np.percentile(x,q)