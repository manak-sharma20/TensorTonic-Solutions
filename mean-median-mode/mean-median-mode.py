import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x=np.array(x)
    a=np.mean(x)
    b=np.median(x)
    freq=Counter(x)
    c=freq.most_common(1)[0][0]
    
    
    return a,b,c
   